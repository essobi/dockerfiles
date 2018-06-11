FROM fedora:27  
RUN DLL_FILES=$(for dll in riched20 riched32 msls31 MSCTF MSCTFP wlanapi
xmllite msxml msxml2 msxml3 msxml6 ole32 oleaut32 olepro32 comctl32 quartz
pngfilt setupapi devenum; do echo WINDOWS/system32/$dll.dll; done); \  
useradd -U -m user; \  
curl -o /etc/yum.repos.d/winehq.repo https://dl.winehq.org/wine-
builds/fedora/27/winehq.repo; \  
dnf install -y winehq-devel $(dnf repoquery -q --requires winetricks | grep -v
^wine) glx-utils mesa-dri-drivers.x86_64 mesa-dri-drivers.i686
/usr/bin/ntlm_auth glibc-langpack-en langpacks-en glibc-langpack-zh langpacks-
zh_CN langpacks-zh_TW p7zip-plugins libXt; \  
dnf clean all; \  
curl -vLo /usr/local/bin/winetricks
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks;
\  
chmod +x /usr/local/bin/winetricks; \  
mkdir -p /opt/wine-devel/share/wine/mono /opt/wine-devel/share/wine/gecko; \  
cd /opt/wine-devel/share/wine/mono; \  
curl -vLOJ https://dl.winehq.org/wine/wine-mono/4.7.1/wine-mono-4.7.1.msi; \  
cd /opt/wine-devel/share/wine/gecko; \  
curl -vLOJ https://dl.winehq.org/wine/wine-
gecko/2.47/wine_gecko-2.47-x86_64.msi; \  
curl -vLOJ https://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi;
\  
cd /tmp; \  
curl -O
https://download.microsoft.com/download/D/7/A/D7AD3FF8-2618-4C10-9398-2810DDE730F7/WindowsXPMode_zh-
cn.exe; \  
curl -O
https://download.microsoft.com/download/B/9/3/B93CD319-CD5A-41C8-9577-39F68D5E8009/WindowsXPMode_zh-
tw.exe; \  
curl -O
https://download.microsoft.com/download/7/2/C/72C7BAB7-2F32-4530-878A-292C20E1845A/WindowsXPMode_en-
us.exe; \  
for lcid in zh-cn zh-tw en-us; do \  
7z e -tcab WindowsXPMode_$lcid.exe sources/xpm; \  
rm WindowsXPMode_$lcid.exe; \  
7z e -tcab xpm VirtualXPVHD; \  
rm xpm; \  
mkdir /opt/$lcid; \  
7z e VirtualXPVHD -o/opt/$lcid $DLL_FILES; \  
rm VirtualXPVHD; \  
done  
USER user  
WORKDIR /home/user  

