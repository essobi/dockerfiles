FROM java:8-jre-alpine  
  
RUN apk upgrade \--update \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add \--no-cache mongodb  
  
VOLUME /data/db  
  
ENTRYPOINT /usr/bin/mongod  

