FROM lsiobase/alpine:3.5  
MAINTAINER sensei73 <sensei73@gmail.com>  
  
# environment variables  
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
  
# install runtime packages  
RUN \  
apk add --no-cache \  
pptpd \  
iptables \  
rsyslog \  
ca-certificates \  
libressl2.4-libssl \  
p7zip \  
unrar \  
unzip && \  
apk add --force --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
pptpclient \  
deluge && \  
  
# install build packages  
apk add \--no-cache --virtual=build-dependencies \  
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
COPY entrypoint.sh /entrypoint.sh  
COPY content /  
RUN chmod 0700 /entrypoint.sh  
  
# ports and volumes  
EXPOSE 8112 58846 58946 58946/udp  
VOLUME /config /downloads  
  
ENTRYPOINT ["/entrypoint.sh"]  

