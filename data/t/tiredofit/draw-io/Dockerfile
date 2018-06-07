FROM tiredofit/nginx  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
  
RUN apk update && \  
apk add --no-cache \  
git && \  
mkdir -p /usr/src && \  
cd /usr/src && \  
git clone \--depth=1 https://github.com/jonberenguer/draw.io.git && \  
rm -rf /www/html && \  
ln -s /usr/src/draw.io/war/ /www/html  
  

