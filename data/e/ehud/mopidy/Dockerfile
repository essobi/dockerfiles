################################################  
#  
#  
#  
#  
#  
################################################  
  
FROM ehudkaldor/alpine-s6:latest  
MAINTAINER Ehud Kaldor <ehud@UnfairFunction.org>  
  
# Server socket.  
EXPOSE 6680  
  
# RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
RUN apk add --update \  
mopidy \  
gcc \  
g++ \  
gst-plugins-good \  
gst-plugins-bad \  
gst-plugins-ugly \  
alsa-utils \  
python \  
python-dev \  
py-cffi \  
py-six \  
py-pip \  
py-lxml && \  
pip install --upgrade pip && \  
pip install Mopidy-MusicBox-Webclient && \  
pip install Mopidy-Mobile && \  
pip install mopidy-beets && \  
pip install mopidy-moped && \  
pip install Mopidy-Local-SQLite && \  
pip install mopidy-gmusic && \  
pip install Mopidy-Local-Images && \  
pip install Mopidy-Iris && \  
apk del \  
libffi-dev \  
openssl-dev \  
build-base \  
gcc \  
g++ \  
py-pip \  
python-dev && \  
rm -rf /var/cache/apk/*  
# Add the configuration file.  
ADD rootfs /  

