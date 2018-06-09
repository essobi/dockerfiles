FROM alpine:latest  
MAINTAINER Jason Wilder <mail@jasonwilder.com>  
  
RUN apk -U add openssl  
  
ENV VERSION v0.0.6-s4s0l  
ENV DOWNLOAD_URL https://github.com/s4s0l/docker-
gen/releases/download/$VERSION/docker-gen-alpine-linux-amd64-$VERSION.tar.gz  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
RUN wget -qO- $DOWNLOAD_URL | tar xvz -C /usr/local/bin  
  
ENTRYPOINT ["/usr/local/bin/docker-gen"]  

