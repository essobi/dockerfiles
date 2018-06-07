FROM alpine:edge  
MAINTAINER dentych  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --no-cache mongodb  
  
VOLUME ["/data/db"]  
  
WORKDIR /data  
  
CMD ["mongod"]  
  
EXPOSE 27017  

