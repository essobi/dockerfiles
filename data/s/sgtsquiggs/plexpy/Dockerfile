FROM sgtsquiggs/alpine:3.4  
MAINTAINER sgtsquiggs  
  
RUN \  
# install packages  
apk add \--no-cache \  
git \  
python \  
py-cryptography \  
py-cffi \  
py-enum34 \  
py-openssl \  
py-six  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /logs  
EXPOSE 8181  

