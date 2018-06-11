# Alpine Linux with redis  
FROM youske/alpine-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="alpine redis image" \  
com.stdmachine.role="radis image"  
  
ENV DATA_DIR=/redis_data \  
LOG_DIR=/redis_log \  
LOGLEVEL=warning \  
DATABASES=8 \  
TIMEOUT=3000 \  
PORT=6379  
RUN PACKAGE="redis" && \  
apk add ${PACKAGE} \--no-cache && \  
mkdir -p ${DATA_DIR} && mkdir -p ${LOG_DIR} && \  
chown -R admin:admin ${DATA_DIR} && chown -R admin:admin ${LOG_DIR} && \  
rm -rf /tmp/* && rm -rf /var/cache/apk/*  
  
COPY redis.conf.tmpl /etc/redis.conf.tmpl  
EXPOSE ${PORT}  
ENTRYPOINT
["render","/etc/redis.conf","--","switch","shell=/bin/bash","--","/init"]  
CMD ["gosu","admin","redis-server"]  

