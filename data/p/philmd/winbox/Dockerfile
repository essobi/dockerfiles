FROM debian:stable  
  
MAINTAINER F4BUG <f4bug@amsat.org>  
  
RUN useradd --home-dir /home/user --create-home user  
  
# wine  
RUN dpkg --add-architecture i386 && \  
apt-get -q update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -y wine32 && \  
apt-get clean  
  
ENV WINE=wine32 WINEARCH=win32 QT_X11_NO_MITSHM=1 WINEDEBUG=fixme-all  
  
RUN ln -s /usr/lib/wine/wineserver32 /usr/local/sbin/wineserver  
  
# winbox  
ADD https://download2.mikrotik.com/routeros/winbox/3.11/winbox.exe
/opt/winbox.exe  
  
ADD winbox-container-helper.sh /opt/winbox-container-helper.sh  
  
RUN chmod 755 /opt/winbox.exe /opt/winbox-container-helper.sh  
  
ENTRYPOINT ["/opt/winbox-container-helper.sh"]  
  
USER user  
RUN mkdir -p ${HOME}/.wine/drive_c/users/user/Application\ Data/Mikrotik  

