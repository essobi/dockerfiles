FROM docker:stable-dind  
  
RUN apk add --no-cache curl py-pip && \  
curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-
machine-Linux-x86_64 > /usr/bin/docker-machine && \  
chmod +x /usr/bin/docker-machine && \  
pip install docker-compose && \  
apk del --purge curl && \  
rm -rf /var/cache/apk/* /lib/apk/db/*  

