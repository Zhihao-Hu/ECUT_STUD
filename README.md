# ECUT_STUD
通过python seleniumweb自动化，以及powershell脚本实现开启点击
准备工作
1.安装好chrome以及chromedrive的版本（https://chromedriver.storage.googleapis.com/index.html）
2.安装python及运行所依赖的库selenium和requests
安装好python后可通过指令安装库
pip install selenium
pip install request
3.将ECUT_STUD.py文件修改后打包成ECUT_STUD.exe
4.打包后的ECUT_STUD.exe;hotspot.ps1;连接及打开热点.bat放在同一个文件夹。
5.右键点击‘连接及打开热点.bat’创建快捷方式，将此快捷方式放进开机自启文件夹路径为C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
注意：如果你使用的是无线连接，应该设置wifi为靠近自动连接。
