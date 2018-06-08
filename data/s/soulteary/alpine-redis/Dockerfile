FROM soulteary/alpine-base:3.4  
MAINTAINER soulteary <soulteary@gmail.com>  
  
ENV REDIS_VERSION 3.2.0-r0  
  
# ref  
# https://github.com/smebberson/docker-alpine/tree/master/alpine-redis  
RUN apk --no-cache --no-progress update && \  
apk add redis=${REDIS_VERSION} && \  
rm -rf /var/cache/apk/* && \  
mkdir /data && \  
chown -R redis:redis /data && \  
echo -e "include /etc/redis-local.conf\n" >> /etc/redis.conf  
  
CMD redis-cli --version  
  
ADD root /  
  
VOLUME ["/data"]  
  
EXPOSE 6379

