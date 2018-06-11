FROM gliderlabs/alpine:3.4  
# https://hub.docker.com/r/gliderlabs/alpine/  
MAINTAINER joan joan@wetopi.com  
  
RUN apk-install \  
mysql-client \  
bash \  
\  
&& echo "===> Removing unused APK resources..." \  
&& rm -rf /var/cache/apk/*  
  
COPY mysql-set-password.sh /usr/local/bin/  
  

