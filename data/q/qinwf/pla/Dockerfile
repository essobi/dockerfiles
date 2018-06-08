FROM debian:sid  
MAINTAINER qin <qin@docker.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i.bak 's/main/main contrib/g' /etc/apt/sources.list && \  
apt-get update && apt-get install -y \  
bzip2 \  
ca-certificates \  
curl \  
flashplugin-nonfree \  
hicolor-icon-theme \  
libasound2 \  
libdbus-glib-1-2 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
xfonts-wqy \  
ttf-wqy-microhei \  
ttf-wqy-zenhei\  
\--no-install-recommends  
  
ENV FIREFOX_VERSION 40.0.2  
ENV LANG zh-CN  
  
RUN curl -sSL
"https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/${LANG}/firefox-${FIREFOX_VERSION}.tar.bz2"
-o /tmp/firefox.tar.bz2 \  
&& mkdir -p /opt/firefox \  
&& tar -xjf /tmp/firefox.tar.bz2 -C /opt/firefox --strip-components 1 \  
&& rm /tmp/firefox.tar.bz2* \  
&& ln -s /opt/firefox/firefox /usr/bin/firefox  
  
COPY local.conf /etc/fonts/local.conf  
  
RUN apt-get install -y -d mate-desktop-environment-core xserver-xorg-video-
vmware && rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

