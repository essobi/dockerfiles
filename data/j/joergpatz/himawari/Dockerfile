FROM node:4.3.1  
MAINTAINER Joerg Patzer <joerg.patzer@me.com>  
  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list \  
&& wget https://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-
multimedia-keyring_2016.3.7_all.deb \  
&& dpkg -i deb-multimedia-keyring_2016.3.7_all.deb \  
&& apt-get update \  
&& apt-get install -y \  
imagemagick \  
graphicsmagick \  
ffmpeg \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* \  
&& npm i -g himawari  
  
WORKDIR /tmp  
  
# define container as an executable  
ENTRYPOINT ["/usr/local/bin/himawari"]

