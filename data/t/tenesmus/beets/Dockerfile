FROM alpine:edge  
MAINTAINER Nathan Douglas <docker@tenesm.us>  
ENV BEETSDIR /config  
RUN set -xe \  
&& apk add --no-cache \  
bash \  
curl \  
faac \  
faad2 \  
ffmpeg \  
flac \  
imagemagick \  
jq \  
lame \  
libvorbis \  
mutagen \  
nano \  
opus \  
py-pip \  
py-gst \  
python \  
&& pip install -U pip \  
&& pip install -U \  
beautifulsoup4 \  
beets \  
discogs-client \  
pathlib \  
pyacoustid \  
pylast \  
https://github.com/ocelma/python-itunes/archive/master.zip \  
pyxdg \  
requests \  
https://github.com/hay/xml2json/zipball/master  
  
VOLUME /config /data /music  

