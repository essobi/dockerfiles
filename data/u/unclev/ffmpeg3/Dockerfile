FROM ubuntu:xenial  
MAINTAINER Victor Kulichenko <onclev@gmail.com>  
ARG PUID=1000  
ARG PGID=1000  
RUN set -x \  
&& apt-get update -qq && apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:jonathonf/ffmpeg-3 \  
&& apt-get update -qq && apt-get install -y ffmpeg libav-tools x264 x265 && rm
-rf /var/lib/apt/lists/* \  
&& groupadd -g $PGID producer && useradd -b /home -m -g $PGID -u $PUID -s
/bin/bash producer  
USER producer  
WORKDIR /home/producer  
VOLUME ["/home/producer"]  
CMD ffmpeg  

