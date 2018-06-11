FROM wiggins/alpine:latest  
MAINTAINER from wiggins  
  
ENV VERSION=4.0.6  
ENV DOWN_URL=http://download.redis.io/releases/redis-${VERSION}.tar.gz \  
TEMP_DIR=/tmp/redis \  
DATA_DIR=/data/redis  
  
RUN set -x && \  
FILE_NAME=${DOWN_URL##*/} && \  
mkdir -p ${TEMP_DIR} ${DATA_DIR} && \  
apk --update --no-cache upgrade && \  
# grab su-exec for easy step-down from root  
apk add \--no-cache 'su-exec>=0.2' openssh && \  
apk add --no-cache --virtual .build-deps gcc linux-headers make musl-dev tar
&& \  
addgroup -S redis && adduser -S -h ${DATA_DIR} -s /sbin/nologin -G redis redis
&& \  
curl -Lk ${DOWN_URL} |tar xz -C ${TEMP_DIR} \--strip-components=1 && \  
cd ${TEMP_DIR} && \  
make -C ${TEMP_DIR} -j $(awk '/processor/{i++}END{print i}' /proc/cpuinfo) &&
\  
make -C ${TEMP_DIR} install && \  
apk del .build-deps tar gcc make && \  
rm -rf /var/cache/apk/* ${TEMP_DIR}  
  
COPY entrypoint.sh /entrypoint.sh  
COPY redis.conf /etc/redis.conf  
  
VOLUME ${DATA_DIR}  
WORKDIR ${DATA_DIR}  
  
EXPOSE 6379/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["redis-server", "/etc/redis.conf"]  

