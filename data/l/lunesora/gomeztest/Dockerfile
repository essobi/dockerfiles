FROM ubuntu:14.04.3  
MAINTAINER Colin  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN dpkg --add-architecture i386  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:ubuntu-wine/ppa \  
&& apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends supervisor \  
openssh-server pwgen sudo vim-tiny \  
net-tools \  
lxde x11vnc xvfb \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
libreoffice firefox \  
fonts-wqy-microhei \  
language-pack-zh-hant language-pack-gnome-zh-hant firefox-locale-zh-hant
libreoffice-l10n-zh-tw \  
nginx \  
python-pip python-dev build-essential \  
wine1.7 winetricks \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD
https://dl.dropboxusercontent.com/u/23905041/x11vnc_0.9.14-1.1ubuntu1_amd64.deb
/tmp/  
ADD https://dl.dropboxusercontent.com/u/23905041/x11vnc-
data_0.9.14-1.1ubuntu1_all.deb /tmp/  
RUN dpkg -i /tmp/x11vnc*.deb  
RUN wget http://lastmile.gomez.com/PEERInstall.exe  
  
ADD web /web/  
RUN pip install -r /web/requirements.txt  
  
ADD noVNC /noVNC/  
ADD nginx.conf /etc/nginx/sites-enabled/default  
ADD startup.sh /  
ADD supervisord.conf /etc/supervisor/conf.d/  
  
EXPOSE 6080  
WORKDIR /root  
ENTRYPOINT ["/startup.sh"]  

