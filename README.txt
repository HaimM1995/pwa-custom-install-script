# build
pyinstaller ./pwa_installer.py --onefile --noconsole --add-binary "./driver/chromedriver.exe;./dist/driver"
