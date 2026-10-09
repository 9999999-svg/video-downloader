from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
command = [sys.executable, '-m', 'PyInstaller', '--noconfirm', '--onefile', '--console', '--name', 'UniversalDL', '--distpath', str(root / 'dist'), '--workpath', str(root / 'build'), '--specpath', str(root / 'build'), '--exclude-module', 'imageio_ffmpeg', '--exclude-module', 'cv2']
command += ['--exclude-module', 'numpy']
command += ['--collect-all', 'yt_dlp']
command.append(str(root / 'universal_downloader.py'))
subprocess.run(command, cwd=root, check=True)
