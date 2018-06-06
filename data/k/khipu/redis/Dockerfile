FROM khipu/base-alpine  
MAINTAINER developers@khipu.com  
  
# based on https://github.com/docker-
library/redis/blob/master/3.2/alpine/Dockerfile  
RUN apk add --no-cache 'su-exec>=0.2'  
  
ENV REDIS_VERSION 3.2.0  
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.2.0.tar.gz  
ENV REDIS_DOWNLOAD_SHA1 0c1820931094369c8cc19fc1be62f598bc5961ca  
  
# for redis-sentinel see: http://redis.io/topics/sentinel  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
linux-headers \  
make \  
musl-dev \  
tar \  
&& wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL" \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/redis \  
&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \  
&& rm redis.tar.gz \  
&& make -C /usr/src/redis \  
&& make -C /usr/src/redis install \  
&& rm -r /usr/src/redis \  
&& apk del .build-deps  
  
RUN mkdir /data && chown khipu:khipu /data  
  
COPY confd /etc/confd  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

