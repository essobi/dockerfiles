FROM alpine:3.7  
MAINTAINER bingo <bingov5@icloud.com>  
  
ADD https://raw.githubusercontent.com/bingozb/nginx-proxy/master/nginx.tmpl
/etc/docker-gen/templates/nginx.tmpl  
RUN apk -U add openssl  
  
ENV VERSION 0.7.4  
ENV DOWNLOAD_URL https://github.com/jwilder/docker-
gen/releases/download/$VERSION/docker-gen-alpine-linux-amd64-$VERSION.tar.gz  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
RUN wget -qO- $DOWNLOAD_URL | tar xvz -C /usr/local/bin  
  
ENTRYPOINT ["/usr/local/bin/docker-gen"]  

