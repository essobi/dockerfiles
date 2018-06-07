FROM python:3.5  
  
#Build windows version of python 3.5  
RUN echo "deb http://deb.debian.org/debian sid main"
>/etc/apt/sources.list.d/sid.list && \  
dpkg --add-architecture i386 && apt update && apt install -t sid -y wine wget
xvfb cabextract unzip && \  
cd /root && wget
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
&& \  
chmod +x winetricks && xvfb-run ./winetricks --force -q vcrun2015 && \  
wget https://github.com/upx/upx/releases/download/v3.91/upx391w.zip && unzip
upx391w.zip && mv upx391w/upx.exe ~/.wine/drive_c/windows && \  
wget
https://sourceforge.net/projects/winpython/files/WinPython_3.5/3.5.2.3/WinPython-64bit-3.5.2.3Zero.exe/download
&& \  
mv download zero.exe && wine64 zero.exe /S && mkdir ~/.wine/drive_c/python &&
mv WinPython-64bit-3.5.2.3Zero/python-3.5.2.amd64/* ~/.wine/drive_c/python &&
\  
cd ~/.wine/drive_c/python && wine python -m pip install --upgrade pip && wine
python -m pip install pyinstaller  
  
  

