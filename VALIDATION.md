# 验证记录

Windows x64、Python 3.14.6，2026-10-10。

本库 universal_downloader.py 和 UniversalDL.exe 与原合集 v1.0.0 逐字节相同，程序实现没有重新修改。独立目录下运行源码与 EXE 的 check.py 实际文件检查均通过，包含 CLI 帮助、中文路径及本工具实际功能输出；媒体使用已存在的 FFmpeg，下载器使用临时本地 HTTP 样本，不宣称所有公共网站或 GUI 已测试。

check.py 可复现本库检查；指定 --exe 检查下载的 EXE，媒体检查可用 --ffmpeg 指定本机可信程序。原合集更广的验证记录保留在总仓库技术文件。
