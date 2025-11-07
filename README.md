iframe 链接格式化工具（自动复制版）​
​
一款轻量、高效的桌面端工具，专为快速处理 iframe 标签设计，自动补全 HTTPS 协议、添加 / 规范 autoplay 参数、优化标签格式，并一键复制结果到剪贴板，大幅提升网页开发 / 内容编辑效率。​
🌟 核心功能​
智能格式化处理​
自动提取 iframe 标签中的 src 属性值，补全 https: 协议（适配 // 开头的链接）​
统一设置 autoplay=0（已存在时自动替换，不存在时追加，避免重复）​
保留原始标签中除 src 外的其他属性（如 scrolling、allowfullscreen 等）​
自动添加优化后的 width="100%" height="480" 属性，适配主流页面布局​
清除多余空格和无效符号，规范标签格式​
高效便捷操作​
格式化完成后自动复制结果到剪贴板，无需手动复制​
支持手动复制功能，按需使用​
一键清空输入 / 输出内容，快速重新操作​
自动关闭的成功提示框，不干扰后续操作​
友好的用户体验​
简洁直观的 GUI 界面，无需命令行操作​
支持 Windows 系统隐藏命令框，避免冗余窗口​
输入区域提供示例参考，降低使用门槛​
完善的错误提示（空输入、无效标签等场景）​
窗口居中显示、置顶提示，操作更顺畅​
📋 适用场景​
网页开发中嵌入视频（如 B 站、腾讯视频等）、音频、第三方组件的 iframe 标签处理​
内容编辑时快速规范 iframe 格式，确保跨平台兼容性​
批量处理 iframe 标签时，减少手动修改的重复工作（如自媒体、网站运营场景）​
🚀 快速使用​
1. 输入格式要求​
需输入完整的 iframe 标签，且包含 src 属性（支持大小写不敏感），示例：​
​
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=123456" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>​
​
2. 操作步骤​
打开工具，在「输入区域」粘贴原始 iframe 标签​
点击「格式化链接（自动复制）」按钮​
提示框显示「格式化完成」后，直接在目标位置粘贴（结果已自动复制）​
如需重新操作，点击「清空内容」即可重置输入 / 输出区域​
3. 输出示例​
输入上述示例后，工具将输出格式化后的标签：​
​
<iframe src="https://player.bilibili.com/player.html?isOutside=true&aid=123456&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="480"></iframe>​
​
📦 安装与运行​
环境要求​
Python 3.6 及以上版本​
依赖库：无（仅使用 Python 标准库 tkinter、re、sys、ctypes，无需额外安装依赖）​
运行方式​
方式 1：直接运行源码​
克隆 / 下载项目源码到本地​
确保本地已安装 Python 3.6+​
双击运行 .py 文件，或在终端执行：​
​
python iframe_formatter.py​
​
方式 2：打包为可执行文件（Windows）​
如需生成无需 Python 环境的 .exe 文件，可使用 pyinstaller 打包：​
安装打包工具：​
​
pip install pyinstaller​
​
执行打包命令（隐藏命令框）：​
​
pyinstaller -w -F iframe_formatter.py​
​
打包完成后，在 dist 目录中找到 .exe 文件，双击即可运行​
⚠️ 注意事项​
仅支持处理完整的 iframe 标签，若输入不完整（如缺少 </iframe> 结尾），会提示「未找到有效的 src 属性值」​
src 属性值需以 // 开头（如 //player.bilibili.com/xxx），工具会自动补全 https:​
若原始标签中已存在 autoplay 参数（如 autoplay=1），工具会自动替换为 autoplay=0​
工具会保留原始标签中的其他属性（如 allowfullscreen、scrolling 等），不会删除或修改​
📌 功能更新日志​
v1.0.0（初始版本）​
支持 iframe 标签 src 协议补全（// → https://）​
自动添加 / 规范 autoplay=0 参数​
优化标签格式，添加固定宽高属性​
自动复制结果到剪贴板​
支持手动复制、清空内容功能​
Windows 系统隐藏命令框​
