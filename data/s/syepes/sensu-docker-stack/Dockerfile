# Usage:  
#  
# docker build --force-rm -t redis .  
# docker run -d --name redis -h redis -p 6379:6379 redis  
FROM alpine:latest  
MAINTAINER Sebastian YEPES <syepes@gmail.com>  
  
  
ENV LANG=en_US.UTF-8 \  
REDIS_VERSION=3.2.3  
RUN apk add --no-cache --virtual build-deps build-base linux-headers openssl
tzdata tar \  
&& apk add --no-cache curl \  
&& rm -f /etc/localtime && ln -s /usr/share/zoneinfo/UTC /etc/localtime \  
&& mkdir /tmp/redis \  
&& curl -#SL http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz |
tar -xz -C /tmp/redis --strip-components 1 \  
&& cd /tmp/redis \  
&& make install \  
&& cp redis.conf /etc/redis.conf \  
&& sed -i -e 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis.conf \  
&& apk del build-deps \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
VOLUME ["/data"]  
WORKDIR ["/data"]  
  
EXPOSE 6379  
CMD ["redis-server", "/etc/redis.conf"]  
  
HEALTHCHECK \--interval=15s --timeout=3s --retries=3 CMD echo -e "PING\r\n"
|nc localhost 6379 |grep +PONG || exit 1  
  

