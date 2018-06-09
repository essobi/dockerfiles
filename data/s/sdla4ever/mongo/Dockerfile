FROM alpine:edge  
  
MAINTAINER Martin Calvert "martinlcalvert@gmail.com"  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache mongodb \  
&& mkdir -p /data/db \  
&& chown -R mongodb /data/db \  
&& chown mongodb /data/db  
  
USER mongodb  
  
EXPOSE 27017  
VOLUME /data/db  
  
CMD ["mongod"]  
  

