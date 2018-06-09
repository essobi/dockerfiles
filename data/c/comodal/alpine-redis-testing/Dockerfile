FROM alpine:edge  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG REDIS_SRC_URL="http://download.redis.io/releases/redis-stable.tar.gz"  
  
LABEL org.label-schema.build-date=$BUILD_DATE\  
org.label-schema.vcs-url="https://github.com/comodal/alpine-redis-
testing.git"\  
org.label-schema.vcs-ref=$VCS_REF\  
org.label-schema.name="Integration Testing Redis Cluster"\  
org.label-schema.description="Convenience image for Redis Cluster integration
tests."\  
org.label-schema.usage="https://github.com/comodal/alpine-redis-
testing#docker-images-for-redis-cluster-testing--"\  
org.label-schema.schema-version="1.0.0-rc.1"  
RUN addgroup -S redis && adduser -S -G redis redis\  
&& mkdir -p /redis/data /redis/modules\  
&& chown redis:redis /redis/data /redis/modules  
  
RUN set -x\  
&& apk add \--no-cache --virtual .build-deps\  
curl\  
gcc\  
linux-headers\  
make\  
musl-dev\  
tar\  
&& curl -o redis.tar.gz "$REDIS_SRC_URL"\  
&& mkdir -p /usr/src/redis\  
&& tar -xzf redis.tar.gz -C /usr/src/redis \--strip-components=1\  
&& rm redis.tar.gz\  
&& make -C /usr/src/redis\  
&& make -C /usr/src/redis install\  
&& rm -r /usr/src/redis\  
&& apk del .build-deps\  
&& apk add \--no-cache bash  
  
VOLUME /redis/data /redis/modules  
WORKDIR /redis/data  
  
ADD entrypoint.sh /entrypoint.sh  
  
USER redis  
  
ENTRYPOINT ["/entrypoint.sh"]  

