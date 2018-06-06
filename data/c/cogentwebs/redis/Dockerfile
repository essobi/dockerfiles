FROM cogentwebs/base  
  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
# Set labels  
LABEL com.redis.cogentwebworks.version="0.1.0-beta"  
  
ENV REDIS_VERSION=4.0.1  
ENV
REDIS_DOWNLOAD_SHA1=2049cd6ae9167f258705081a6ef23bb80b7eff9ff3d0d7481e89510f27457591  
  
  
### Files Addition  
ADD rootfs /  
  
## Redis Installation  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S redis && adduser -S -G redis redis  
  
RUN apk-install redis su-exec && apk-clean  
  
#Volume Setup  
VOLUME ["/usr/local/redis/"]  
  
## Networking Configuration  
EXPOSE 6379  
### Entrypoint Configuration  
ENTRYPOINT ["/init"]  

