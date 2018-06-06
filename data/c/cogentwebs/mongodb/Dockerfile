FROM cogentwebs/base  
  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
# Set labels  
LABEL com.mongodb.cogentwebworks.version="0.1.0-beta"  
  
### Files Addition  
ADD rootfs /  
  
## Redis Installation  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S mongodb && adduser -S -G mongodb mongodb  
  
RUN apk-install mongodb su-exec && \  
rm /usr/bin/mongoperf && \  
apk-clean  
  
#Volume Setup  
VOLUME ["/data/db"]  
  
## Networking Configuration  
EXPOSE 27017 28017  
### Entrypoint Configuration  
ENTRYPOINT ["/init"]  

