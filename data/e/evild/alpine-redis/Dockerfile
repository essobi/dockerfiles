FROM evild/alpine-base:1.0.0  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S redis && adduser -S -G redis redis  
  
ENV REDIS_VERSION 3.0.7  
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.0.7.tar.gz  
ENV REDIS_DOWNLOAD_SHA1 e56b4b7e033ae8dbf311f9191cf6fdf3ae974d1c  
  
# for redis-sentinel see: http://redis.io/topics/sentinel  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
linux-headers \  
make \  
musl-dev \  
&& wget "$REDIS_DOWNLOAD_URL" -O redis.tar.gz \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src \  
&& tar -xzf redis.tar.gz -C /usr/src \  
&& mv "/usr/src/redis-$REDIS_VERSION" /usr/src/redis \  
&& rm redis.tar.gz \  
&& make -C /usr/src/redis \  
&& make -C /usr/src/redis install \  
&& rm -r /usr/src/redis \  
&& apk del .build-deps  
  
ADD root /  
RUN mkdir /data && chown redis:redis /data  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 6379  

