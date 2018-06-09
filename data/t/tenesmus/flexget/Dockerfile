FROM alpine:latest  
MAINTAINER Nathan Douglas <docker@tenesm.us>  
  
RUN set -xe \  
&& mkdir -p /config \  
&& mkdir -p /scripts \  
&& apk add \--no-cache \  
ca-certificates \  
python-dev \  
py-pip \  
mutagen \  
ffmpeg \  
bash \  
&& pip install --upgrade pip \  
&& pip install flexget \  
transmissionrpc \  
python-telegram-bot \  
eyed3 \  
&& touch /config/config.yml  
VOLUME /config  
VOLUME /scripts  
VOLUME /download  
ENTRYPOINT []  
CMD ["/usr/bin/flexget", "--loglevel", "info", "-c", "/config/config.yml",
"daemon", "start"]  
  

