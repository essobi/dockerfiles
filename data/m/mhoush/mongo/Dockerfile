#FROM alpine:edge  
FROM mongo:latest  
MAINTAINER https://github.com/m-housh  
  
COPY entrypoint.sh /entrypoint.sh  
  
#RUN echo 'http://dl-3.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
# apk add --no-cache mongodb  
VOLUME /data/db  
EXPOSE 27017 28017  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mongod"]  

