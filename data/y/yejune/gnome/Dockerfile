FROM ubuntu:16.04  
MAINTAINER yejune "kwon@yejune.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
software-properties-common build-essential \  
ubuntu-desktop \  
gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal \  
tightvncserver sudo \  
fonts-nanum fonts-nanum-coding \  
language-selector-gnome \  
chromium-browser firefox xterm gedit \  
language-pack-ko \  
language-pack-gnome-ko \  
chromium-browser-l10n \  
fcitx-frontend-gtk3 \  
ibus-hangul \  
fcitx-frontend-qt4 \  
fcitx-frontend-qt5 \  
fcitx \  
fcitx-hangul \  
firefox-locale-ko \  
hunspell-ko \  
fonts-unfonts-core \  
fcitx-ui-classic \  
fcitx-frontend-gtk2 \  
dbus xfonts-100dpi xfonts-75dpi xfonts-cyrillic dbus-x11 \  
ibus dconf-tools  
  
RUN locale-gen ko_KR.UTF-8  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
RUN mkdir /root/.vnc  
ADD xstartup /root/.vnc/xstartup  
  
ADD run.sh /run.sh  
RUN chmod 777 /run.sh  
CMD /run.sh  
  
RUN echo 'alias chrome="chromium-browser --no-sandbox --user-data-dir=/tmp"'
>> ~/.bashrc  
  
EXPOSE 5901  

