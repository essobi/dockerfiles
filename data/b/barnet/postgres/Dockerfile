# alpine:3.7  
FROM postgres:10.2-alpine  
  
# COPY ./postgresql.conf.sample
/usr/local/share/postgresql/postgresql.conf.sample  
  
# COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
# set timezone and add git  
RUN apk add --update \--no-cache git tzdata && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
apk del tzdata

