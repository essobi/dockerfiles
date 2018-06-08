FROM sgtsquiggs/alpine:3.4  
MAINTAINER sgtsquiggs  
  
RUN \  
# install packages  
apk add \--no-cache \  
nodejs \  
git  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 3000  
VOLUME /config  

