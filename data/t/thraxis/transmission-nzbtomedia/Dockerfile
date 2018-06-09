FROM lsiobase/alpine.python:3.6  
MAINTAINER Thraxis  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Thraxis' version:- ${VERSION} Build-date:- ${BUILD_DATE}"  
  
# install packages  
RUN \  
apk add --no-cache \  
jq \  
transmission-cli \  
transmission-daemon && \  
  
git -C /app clone -q https://github.com/clinton-hall/nzbToMedia.git && \  
rm -rf /var/cache/apk/* /tmp/*  
  
# copy local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 9091 51413  
VOLUME /config /downloads /watch  

