# VERSION: 0.1  
# DESCRIPTION: Create Thunderbird container
(https://www.mozilla.org/thunderbird/)  
# AUTHOR: Julien Giovaresco <dev@giovaresco.fr>  
#  
# Usage  
#  
# docker run -d \  
# --net host \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v $HOME/.thunderbird/mozilla:/root/.mozilla \  
# -v $HOME/.thunderbird/thunderbird:/root/.thunderbird \  
# -e DISPLAY=unix$DISPLAY \  
# --device /dev/snd \  
# --device /dev/dri \  
# --name thunderbird \  
# jgiovaresco/thunderbird  
  
FROM jgiovaresco/debian-with-dockerize:latest  
MAINTAINER Julien Giovaresco <dev@giovaresco.fr>  
  
RUN apt-get update && apt-get -y install \  
bzip2 \  
ca-certificates \  
curl \  
tar \  
hicolor-icon-theme \  
libasound2 \  
libdbus-glib-1-2 \  
libfreetype6 \  
libfontconfig \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libgtk2.0-0 \  
libxcomposite1 \  
libxrender1 \  
libxt6 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV THUNDERBIRD_VERSION 38.3.0  
ENV LANG en-US  
  
RUN curl -sSL
"http://releases.mozilla.org/pub/thunderbird/releases/${THUNDERBIRD_VERSION}/linux-x86_64/${LANG}/thunderbird-${THUNDERBIRD_VERSION}.tar.bz2"
-o /tmp/thunderbird.tar.bz2 \  
&& mkdir -p /opt/thunderbird \  
&& tar -xjf /tmp/thunderbird.tar.bz2 -C /opt/thunderbird --strip-components 1
\  
&& rm /tmp/thunderbird.tar.bz2* \  
&& ln -s /opt/thunderbird/thunderbird /usr/bin/thunderbird  
  
ENTRYPOINT [ "/usr/bin/thunderbird" ]  

