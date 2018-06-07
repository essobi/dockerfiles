FROM wernight/plex-media-server:latest  
MAINTAINER Andrea Cattaneo <andrea.cattaneo.dev@gmail.com>  
  
USER root  
  
RUN set -x \  
&& apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
rlwrap \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L 'https://plex.tv/downloads/latest/1?channel=8&build=linux-
ubuntu-x86_64&distro=ubuntu' -o plexmediaserver.deb \  
&& dpkg -i plexmediaserver.deb \  
&& rm -f plexmediaserver.deb  
  
# INSTALL nodejs  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash - \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
USER plex  

