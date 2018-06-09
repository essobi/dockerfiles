FROM systematicchaos/debian-nodejs-zeromq:latest  
MAINTAINER Javier Fernández-Bravo Peñuela <fraferp9@posgrado.upv.es>  
LABEL description="Docker image of Debian + NodeJS and ZeroMQ + Redis"  
  
# add our user and group first to kame sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r redis && useradd -r -g redis redis  
  
# grab gosu for easy step-down from root  
# https://github.com/tianon/gosu/releases  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
chmod +x /usr/local/bin/gosu; \  
gosu nobody true;  
  
ENV REDIS_VERSION 4.0.6  
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-4.0.6.tar.gz  
ENV REDIS_DOWNLOAD_SHA
769b5d69ec237c3e0481a262ff5306ce30db9b5c8ceb14d1023491ca7be5f6fa  
  
# for redis-sentinel see: http://redis.io/topics/sentinel  
RUN set -ex; \  
\  
wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL"; \  
echo "$REDIS_DOWNLOAD_SHA *redis.tar.gz" | sha256sum -c -; \  
mkdir -p /usr/src/redis; \  
tar -xzvf redis.tar.gz -C /usr/src/redis --strip-components=1; \  
rm redis.tar.gz; \  
\  
# disable Redis protected mode [1] as it is unnecesary in the context of
Docker  
# (ports are not automatically exposed when running inside Docker, but rather
explicitly by specifying -p / -P)  
# [1]:
https://github.com/antirez/redis/commit/edd4d555df57dc84265fdfb4ef59a4678832f6da  
grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 1$'
/usr/src/redis/src/server.h; \  
sed -ri 's!^(#define CONFIG_DEFAULT_PROTECTED_MODE) 1$!\1 0!'
/usr/src/redis/src/server.h; \  
grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 0$'
/usr/src/redis/src/server.h; \  
# for future reference, we modify this directly in the source instead of just
supplying a default configuration flag because apparently "if you specify any
argument to redis-server, [it assumes] you are going to specify everything"  
# see also https://github.com/docker-
library/redis/issues/4~issuecomment-50780840  
# (more exactly, this makes sure the default behavior of "save on SIGTERM"
stays functional by default)  
\  
make -C /usr/src/redis -j `nproc`; \  
make -C /usr/src/redis install; \  
\  
rm -r /usr/src/redis;  
  
COPY ./redis-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
RUN mkdir /data && chown redis:redis /data  
WORKDIR /data  
  
EXPOSE 6379  
CMD ["redis-server"]  

