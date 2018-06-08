FROM lsiobase/alpine.python:3.6  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# set python to use utf-8 rather than ascii.  
ENV PYTHONIOENCODING="UTF-8"  
# install runtime packages  
RUN apk add --no-cache \  
py2-crypto \  
py2-curl  
  
# install app  
RUN \  
git clone -b stable https://github.com/pyload/pyload /app/pyload  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 8000 7227 9666  
WORKDIR /app/pyload  
VOLUME /config /downloads  

