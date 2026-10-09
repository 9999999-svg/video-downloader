# 依赖及卸载

Python 源码使用 Python 3.14.6 和 Tkinter，构建使用 PyInstaller 6.21.0（约 4.9 MiB）。Python 本体安装体积随发行方式变化，不确定。本轮复用已安装环境，没有下载新依赖。

| 运行组件 | 固定版本 | 约安装占用 | 状态 |
| --- | --- | --- | --- |
| yt-dlp | 2026.7.4 | 21.2 MiB | 已下载、已安装，复用 |
| imageio-ffmpeg | 0.6.0 | 83.7 MiB | 已下载、已安装，复用 |

PyInstaller 的构建依赖已安装、复用：altgraph 0.17.5（约 0.1 MiB）、packaging 26.2（0.8 MiB）、pefile 2024.8.26（0.7 MiB）、pyinstaller-hooks-contrib 2026.6（1.1 MiB）、pywin32-ctypes 0.2.3（0.2 MiB）、setuptools 83.0.0（7.1 MiB）。

EXE 不捆绑 FFmpeg；将可信 ffmpeg.exe 放在 EXE 同目录或 PATH。FFmpeg 体积随构建不同，不确定；源码 imageio-ffmpeg 0.6.0 可提供 FFmpeg，约 31.2 MB 下载、83.7 MiB 安装，已下载。本任务仅在虚拟环境复用。

本次 EXE UniversalDL.exe：26,082,394 字节，未签名，内含 Python 与 Tcl/Tk 运行时。

删除 EXE 与相关下载文件即可卸载。源码使用自建虚拟环境，关闭程序后删除 .venv 及工具目录即可，不改全局 Python。若自己安装 FFmpeg，删除其目录，并移除自行添加的 PATH 项。工具不添加服务、启动项或系统 PATH。
