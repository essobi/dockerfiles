FROM dorowu/ubuntu-desktop-lxde-vnc  
MAINTAINER haoling  
  
RUN apt-get update &&\  
apt-get install -y language-pack-ja-base language-pack-ja manpages-ja \  
fonts-droid libxss1 libappindicator1 libindicator7 fonts-liberation wget \  
libcurl3 xdg-utils libnspr4 libnss3 gconf-service gconf-service-backend
gconf2-common libgconf-2-4 &&\  
update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja &&\  
apt-get autoclean &&\  
apt-get autoremove &&\  
rm -rf /var/lib/apt/lists/*  
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
/src/google-chrome-stable_current_amd64.deb  
RUN dpkg -i '/src/google-chrome-stable_current_amd64.deb' && \  
rm -rf /src/*.deb  
ADD google-chrome.desktop /usr/share/applications/google-chrome.desktop  
RUN mkdir ~/chrome-data  
  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  

