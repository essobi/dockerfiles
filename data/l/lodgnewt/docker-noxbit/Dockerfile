FROM lsiobase/alpine:3.7  
MAINTAINER lodgnewt  
  
# install packages and symlink libs  
RUN \  
apk add --no-cache \  
curl \  
tar && \  
mkdir -p \  
/opt/noxbit && \  
# install noxbit  
curl -o \  
/tmp/noxbit.tar.gz -L \  
"http://download.noxbit.com/noxbit-pa-x86-64.tar.gz" && \  
tar xf \  
/tmp/noxbit.tar.gz \  
-C /opt/noxbit && \  
# cleanup  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 6689  
VOLUME /config  

