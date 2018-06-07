FROM alpine:3.5  
MAINTAINER Mikkel Oscar Lyderik Larsen <m@moscar.net>  
  
# install runtime packages  
RUN \  
apk add --no-cache \  
ca-certificates \  
p7zip \  
unrar \  
unzip && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/main \  
libressl2.5-libssl && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
deluge && \  
# install build packages  
apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
libffi-dev \  
libressl-dev \  
py2-pip \  
python2-dev && \  
# install pip packages  
pip install --no-cache-dir -U \  
incremental \  
pip && \  
pip install --no-cache-dir -U \  
crypto \  
mako \  
markupsafe \  
pyopenssl \  
service_identity \  
six \  
twisted \  
zope.interface && \  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root/.cache  

