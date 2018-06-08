FROM ubuntu:16.04  
MAINTAINER yejune "kwon@yejune.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install python-software-properties software-properties-common  
RUN apt-add-repository ppa:ubuntu-mate-dev/xenial-mate  
RUN apt-get update && \  
apt-get dist-upgrade -y  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ubuntu-mate-core ubuntu-mate-desktop \  
tightvncserver \  
fonts-nanum \  
fonts-nanum-coding  
  
RUN apt-get install -y language-selector-gnome \  
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
  
RUN apt-get install -y xdm mate-desktop-environment-extras thunderbird-locale-
ko libreoffice-l10n-ko libreoffice-help-ko  
  
RUN locale-gen ko_KR.UTF-8  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
RUN mkdir /root/.vnc  
  
#RUN service dbus start  
ADD run.sh /run.sh  
RUN chmod 777 /run.sh  
CMD /run.sh  
  
RUN echo 'alias chrome="chromium-browser --user-data-dir=/tmp"' >> ~/.bashrc  
  
EXPOSE 5901  

