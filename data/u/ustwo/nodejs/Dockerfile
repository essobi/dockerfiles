FROM alpine:3.2  
MAINTAINER Arnau Siches <arnau@ustwo.com>  
  
RUN adduser -D ustwo \  
&& addgroup ustwo ustwo  
  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& apk add --update \  
nodejs=4.1.1-r0 \  
nodejs-dev=4.1.1-r0 \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /home/ustwo  
EXPOSE 8888  
CMD ["node"]  

