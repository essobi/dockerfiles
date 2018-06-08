FROM ubuntu:14.04.3  
MAINTAINER Fillerino <fillerix99@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /home/ubuntu  
  
# built-in packages  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends software-properties-
common curl \  
&& sudo sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >>
/etc/apt/sources.list.d/arc-theme.list" \  
&& curl -SL
http://download.opensuse.org/repositories/home:Horst3180/xUbuntu_16.04/Release.key
| sudo apt-key add - \  
&& add-apt-repository ppa:fcwu-tw/ppa \  
&& apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends \  
supervisor \  
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
mesa-utils libgl1-mesa-dri \  
gnome-themes-standard gtk2-engines-pixbuf gtk2-engines-murrine pinta arc-theme
\  
chromium-browser wget unzip\  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
RUN cd /home/ubuntu && wget
http://www.otohits.net/dl/OtohitsApp_Linux_3100_B.zip && unzip
OtohitsApp_Linux_3100_B.zip && cd OtohitsApp && wget
https://raw.githubusercontent.com/Fillerix99/sstorage/master/otohits.ini  
RUN cd /usr/share/applications && wget
https://raw.githubusercontent.com/Fillerix99/sstorage/master/surf.desktop  
ADD web /web/  
RUN pip install setuptools wheel && pip install -r /web/requirements.txt  
  
# tini for subreap  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
RUN chmod +x /bin/tini  
  
ADD noVNC /noVNC/  
ADD nginx.conf /etc/nginx/sites-enabled/default  
ADD startup.sh /  
ADD supervisord.conf /etc/supervisor/conf.d/  
ADD doro-lxde-wallpapers /usr/share/doro-lxde-wallpapers/  
ADD gtkrc-2.0 /home/ubuntu/.gtkrc-2.0  
  
EXPOSE 6080  
WORKDIR /root  
ENTRYPOINT ["/startup.sh"]  

