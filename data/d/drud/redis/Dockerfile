FROM ubuntu:14.04  
MAINTAINER Brad Bowman <brad@newmediadenver.com>  
  
ENV REDIS_VERSION 3.0.7  
ENV REDIS_SHA256
b2a791c4ea3bb7268795c45c6321ea5abcc24457178373e6a6e3be6372737f23  
  
COPY files/redis-${REDIS_VERSION}.tar.gz /tmp/redis-${REDIS_VERSION}.tar.gz  
  
RUN echo "${REDIS_SHA256} /tmp/redis-${REDIS_VERSION}.tar.gz" | sha256sum -c -
\  
&& apt-get update \  
&& apt-get install -y make g++ \  
&& apt-get clean -y \  
&& cd /tmp \  
&& tar xvzf redis-${REDIS_VERSION}.tar.gz \  
&& cd redis-${REDIS_VERSION} \  
&& make \  
&& make install \  
&& cp -f src/redis-sentinel /usr/local/bin \  
&& mkdir -p /etc/redis \  
&& cp -f *.conf /etc/redis \  
&& rm -rf /tmp/redis-${REDIS_VERSION}* \  
&& sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf \  
&& sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf \  
&& sed -i 's/^\\(dir .*\\)$/# \1\ndir \/data/' /etc/redis/redis.conf \  
&& sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf  
  
EXPOSE 6379  
CMD ["redis-server", "/etc/redis/redis.conf"]  
VOLUME ["/data"]  
WORKDIR /data  

