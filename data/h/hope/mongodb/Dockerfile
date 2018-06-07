FROM hope/base-alpine:3.4  
MAINTAINER Sergey Sadovoi <sergey@hope.ua>  
  
ENV MONGO_VERSION=3.2.10  
RUN \  
apk add --no-cache mongodb@edge mongodb-tools@edge libgcc@edge libstdc++@edge  
  
VOLUME /data/db  
EXPOSE 27017  
ENTRYPOINT ["/usr/bin/mongod"]  

