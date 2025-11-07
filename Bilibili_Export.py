
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import re

# 仅在Windows系统下隐藏命令框
if sys.platform.startswith('win'):
    import ctypes
    # 调用Windows API隐藏控制台窗口
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def format_iframe_link(input_content):
    """
    专门处理指定格式的输入：完整iframe标签
    核心逻辑：提取src值→补全https→添加autoplay→重组标签
    """
    input_clean = input_content.strip()
    if not input_clean:
        raise ValueError("输入内容不能为空")
    
    # 第一步：提取src属性值（精准匹配双引号包裹的//开头链接）
    src_match = re.search(r'src="(//.*?)"', input_clean, flags=re.IGNORECASE | re.DOTALL)
    if not src_match:
        raise ValueError("未找到有效的src属性值！请输入正确格式的iframe标签")
    
    # 第二步：处理src值
    src_value = src_match.group(1)
    # 添加https:
    if src_value.startswith('//'):
        src_value = 'https:' + src_value
    # 添加&autoplay=0（去重处理）
    if '&autoplay=' not in src_value:
        src_value += '&autoplay=0'
    else:
        src_value = re.sub(r'&autoplay=\d+', '&autoplay=0', src_value)
    
    # 第三步：提取原标签中的其他属性（除了src）
    # 匹配src之后到</iframe>之前的所有内容（排除多余的>）
    other_attrs_match = re.search(r'src="[^"]*"\s+(.*?)\s*</iframe>', input_clean, flags=re.IGNORECASE | re.DOTALL)
    other_attrs = other_attrs_match.group(1).strip() if other_attrs_match else ''
    # 移除可能存在的多余>符号
    other_attrs = other_attrs.replace('>', '').strip()
    
    # 第四步：重组完整的iframe标签（正确拼接，无多余符号）
    if other_attrs:
        final_iframe = f'<iframe src="{src_value}" {other_attrs} width="100%" height="480"></iframe>'
    else:
        final_iframe = f'<iframe src="{src_value}" width="100%" height="480"></iframe>'
    
    # 去除多余的空格（优化格式）
    final_iframe = re.sub(r'\s+', ' ', final_iframe).strip()
    
    return final_iframe

def copy_to_clipboard(content):
    """复制内容到剪贴板（通用函数）"""
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()

def show_auto_close_message(title, message, delay=3000):
    """显示自动关闭的提示框"""
    # 创建顶层窗口作为提示框
    msg_window = tk.Toplevel(root)
    msg_window.title(title)
    msg_window.geometry("300x100")
    msg_window.resizable(False, False)
    
    # 居中显示
    msg_window.update_idletasks()
    x = (root.winfo_screenwidth() - msg_window.winfo_width()) // 2
    y = (root.winfo_screenheight() - msg_window.winfo_height()) // 2
    msg_window.geometry(f"+{x}+{y}")
    
    # 添加提示信息
    msg_label = ttk.Label(msg_window, text=message, font=("Arial", 11))
    msg_label.pack(expand=True)
    
    # 3秒后自动关闭窗口
    msg_window.after(delay, msg_window.destroy)
    
    # 设置窗口置顶，确保用户能看到
    msg_window.attributes('-topmost', True)

def process_link():
    """处理输入的链接，完成格式化并自动复制"""
    input_content = link_entry.get("1.0", tk.END).strip()
    if not input_content:
        messagebox.showwarning("警告", "请输入需要处理的iframe标签！")
        return

    try:
        final_iframe = format_iframe_link(input_content)
        # 清空输出框并显示结果
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, final_iframe)
        # 自动选中结果方便复制（保留手动复制的便利性）
        result_text.tag_add(tk.SEL, "1.0", tk.END)
        # 自动复制到剪贴板
        copy_to_clipboard(final_iframe)
        # 显示3秒后自动关闭的提示框
        show_auto_close_message("成功", "格式化完成！\n结果已自动复制到剪贴板～")
    except Exception as e:
        messagebox.showerror("错误", f"处理失败：{str(e)}")

def clear_content():
    """清空输入框和输出框"""
    link_entry.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)

# 保留手动复制功能（按需使用）
def manual_copy_to_clipboard():
    """手动复制输出框中的结果到剪贴板"""
    result_content = result_text.get("1.0", tk.END).strip()
    if not result_content:
        messagebox.showwarning("警告", "没有可复制的内容！")
        return
    
    copy_to_clipboard(result_content)
    # 手动复制也使用自动关闭提示框
    show_auto_close_message("成功", "结果已复制到剪贴板！", delay=2000)

# 创建主窗口
root = tk.Tk()
root.title("iframe链接格式化工具（自动复制版）")
root.geometry("800x500")
root.resizable(False, False)

# 配置样式
style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 10))

# 输入区域
input_label = ttk.Label(root, text="请输入原始iframe标签（带src属性）：")
input_label.pack(pady=(20, 5), anchor="w", padx=30)

link_entry = tk.Text(root, width=90, height=5, font=("Arial", 10))
link_entry.pack(pady=5, padx=30)

# 功能按钮区域
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

process_btn = ttk.Button(button_frame, text="格式化链接（自动复制）", command=process_link)
process_btn.grid(row=0, column=0, padx=10)

copy_btn = ttk.Button(button_frame, text="手动复制结果", command=manual_copy_to_clipboard)
copy_btn.grid(row=0, column=1, padx=10)

clear_btn = ttk.Button(button_frame, text="清空内容", command=clear_content)
clear_btn.grid(row=0, column=2, padx=10)

# 输出区域
result_label = ttk.Label(root, text="格式化后的iframe代码（已自动复制）：")
result_label.pack(pady=(10, 5), anchor="w", padx=30)

result_text = tk.Text(root, width=90, height=8, font=("Arial", 10))
result_text.pack(pady=5, padx=30)

# 示例提示（匹配你的输入格式）
example_label = ttk.Label(root, text="示例输入：<iframe src=\"//player.bilibili.com/player.html?isOutside=true&aid=xxx\" scrolling=\"no\" border=\"0\" frameborder=\"no\" framespacing=\"0\" allowfullscreen=\"true\"></iframe>", 
                         font=("Arial", 8), foreground="#666")
example_label.pack(pady=(5, 10), anchor="w", padx=30)

# 运行主循环
root.mainloop()
