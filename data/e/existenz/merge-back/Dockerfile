FROM alpine:3.6  
MAINTAINER docker@stefan-van-essen.nl  
  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US.UTF-8' TERM='xterm'
DOCKER_HOST='docker'  
RUN apk -U add git openssh  
  
COPY merge-back.sh /usr/local/bin/merge-back  

