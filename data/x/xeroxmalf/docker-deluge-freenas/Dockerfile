FROM lsiobase/alpine.python:3.5  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1.3.14" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="58846:58846/tcp,58946:58946/tcp,58946:58946/udp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/downloads\", \  
\"descr\": \"Downloads volume\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone - eg Europe/London\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GroupID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"UserID\", \  
\"optional\": true \  
} \  
]"  
  
# environment variables  
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"  
  
# install runtime packages  
RUN \  
apk add --no-cache \  
ca-certificates \  
libressl2.4-libssl \  
p7zip \  
unrar \  
unzip && \  
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
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 58846 58946 58946/udp  
VOLUME /config /downloads  

