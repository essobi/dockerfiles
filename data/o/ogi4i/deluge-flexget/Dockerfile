FROM lsiobase/alpine:3.6  
  
# environment variables  
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"  
  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
libffi-dev \  
openssl-dev \  
py2-pip \  
python2-dev \  
libxml2-dev \  
libxslt-dev && \  
  
# install runtime packages  
apk add --no-cache \  
ca-certificates \  
openssl \  
p7zip \  
unrar \  
unzip \  
cifs-utils \  
nano \  
rsync \  
cdrkit \  
py2-lxml && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
deluge && \  
  
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
zope.interface \  
flexget \  
subliminal \  
kinopoiskpy \  
python-telegram-bot && \  
  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root/.cache  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 8112 58846 53160 53160/udp  
VOLUME /config /downloads /flexcfg  

