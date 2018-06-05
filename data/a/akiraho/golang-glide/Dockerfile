FROM golang:1.10.1-alpine3.7  
# glide  
RUN GLIDE_VERSION=0.13.1 && \  
FILE=glide-v$GLIDE_VERSION-linux-amd64.tar.gz && \  
apk update && \  
apk add openssl git && \  
echo ========== && \  
echo FILE=$FILE && \  
echo ========== && \  
mkdir -p /opt/glide && \  
cd /opt/glide && \  
wget
https://github.com/Masterminds/glide/releases/download/v$GLIDE_VERSION/$FILE
&& \  
tar xvfpz $FILE && \  
rm $FILE && \  
ln -s /opt/glide/linux-amd64/glide /usr/local/bin/glide  

