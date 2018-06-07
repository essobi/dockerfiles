FROM lsiobase/alpine:3.7  
MAINTAINER sparklyballs  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
g++ \  
gcc \  
libffi-dev \  
libressl-dev \  
make \  
python2-dev \  
tar && \  
  
# install runtime packages  
apk add \--no-cache \  
libffi \  
libressl \  
py2-pip && \  
  
# install nntp2nntp via pip package manager  
pip install --no-cache-dir -U \  
https://sourceforge.net/projects/nntp2nntp/files/nntp2nntp-0.3.tar.gz \  
service_identity && \  
  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/root/.cache \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 1563  
VOLUME /config  

