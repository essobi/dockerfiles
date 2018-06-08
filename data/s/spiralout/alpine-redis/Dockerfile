#  
# Small redis docker image based on alpine linux  
#  
# http://github.com/tenstartups/alpine-redis-docker  
#  
FROM alpine:latest  
  
MAINTAINER Marc Lennox <marc.lennox@gmail.com>  
  
# Install packages  
RUN \  
apk --update add redis wget && \  
wget --no-check-certificate -O /usr/local/bin/gosu
https://github.com/tianon/gosu/releases/download/1.4/gosu-amd64 && \  
chmod +x /usr/local/bin/gosu && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /data && chown redis:redis /data  
  
VOLUME /data  
  
WORKDIR /data  
  
COPY entrypoint.sh /docker-entrypoint  
  
ENTRYPOINT ["/docker-entrypoint"]  
  
EXPOSE 6379  
CMD ["redis-server"]  

