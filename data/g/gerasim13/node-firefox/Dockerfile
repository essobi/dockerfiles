FROM selenium/node-firefox  
  
USER root  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe
restricted multiverse" > /etc/apt/sources.list  
RUN apt-get update && \  
apt-get upgrade && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove  
RUN apt-get install -y ubuntu-restricted-extras  
RUN apt-get install --only-upgrade -y firefox  
  
COPY install_flash_player_11_linux.x86_64.tar.gz
install_flash_player_11_linux.x86_64.tar.gz  
RUN mkdir ~/install_flash_player_11_linux && tar -zxvf
install_flash_player_11_linux.x86_64.tar.gz -C ~/install_flash_player_11_linux  
RUN mkdir /usr/lib/flash-plugin/ && \  
cd ~/install_flash_player_11_linux && \  
cp -r usr/* /usr && \  
mkdir -p /usr/lib/flash-plugin/ && \  
mkdir -p /usr/lib/firefox/browser/plugins/ && \  
cp libflashplayer.so /usr/lib/flash-plugin/ && \  
cp libflashplayer.so /usr/lib/firefox/browser/plugins/ && \  
chmod 775 /usr/lib/flash-plugin/libflashplayer.so && \  
chmod 775 /usr/lib/firefox/browser/plugins/libflashplayer.so  
# USER seluser  

