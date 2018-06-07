FROM alpine:edge  
MAINTAINER Paul Liljenberg "liljenberg.paul@gmail.com"  
ENV JOHN_VERSION 1.8.0-r3  
RUN mkdir -p /usr/share/john # Fixes a bug where the directories needed is not
created.  
RUN apk --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing add
john=${JOHN_VERSION}  
  
CMD ["john"]  

