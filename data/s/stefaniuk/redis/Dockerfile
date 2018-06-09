FROM stefaniuk/ubuntu:16.04-20160926  
MAINTAINER daniel.stefaniuk@gmail.com  
# SEE: https://github.com/docker-library/redis/blob/master/3.2/Dockerfile  
ARG APT_PROXY  
ENV REDIS_VERSION="3.2.3" \  
REDIS_DOWNLOAD_URL="http://download.redis.io/releases" \  
REDIS_DOWNLOAD_SHA1="92d6d93ef2efc91e595c8bf578bf72baff397507"  
COPY assets/etc/redis/redis.conf /etc/redis/redis.conf  
COPY assets/etc/redis/sentinel.conf /etc/redis/sentinel.conf  
  
RUN set -ex \  
\  
&& buildDeps=' \  
gcc \  
libc6-dev \  
make \  
' \  
&& if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy \"$APT_PROXY\";
};" >> /etc/apt/apt.conf.d/00proxy; fi \  
&& apt-get --yes update \  
&& apt-get --yes install $buildDeps \  
\  
&& wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL/redis-$REDIS_VERSION.tar.gz" \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/redis \  
&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \  
&& rm redis.tar.gz \  
&& grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 1$'
/usr/src/redis/src/server.h \  
&& sed -ri 's!^(#define CONFIG_DEFAULT_PROTECTED_MODE) 1$!\1 0!'
/usr/src/redis/src/server.h \  
&& grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 0$'
/usr/src/redis/src/server.h \  
&& make -C /usr/src/redis \  
&& make -C /usr/src/redis install \  
&& rm -r /usr/src/redis \  
&& sed 's/^bind 127.0.0.1/bind 0.0.0.0/' -i /etc/redis/redis.conf \  
&& sed 's/^# unixsocket \/tmp\/redis.sock/unixsocket
\/run\/redis\/redis.sock/' -i /etc/redis/redis.conf \  
&& sed 's/^# unixsocketperm 700/unixsocketperm 777/' -i /etc/redis/redis.conf
\  
\  
&& apt-get purge --yes --auto-remove $buildDeps \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/* \  
&& rm -f /etc/apt/apt.conf.d/00proxy  
  
WORKDIR /var/lib/redis  
VOLUME [ "/var/lib/redis" ]  
EXPOSE 6379 26379  
COPY assets/sbin/bootstrap.sh /sbin/bootstrap.sh  
CMD [ "redis-server", "/etc/redis/redis.conf" ]  
  
### METADATA
###################################################################  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
version=$VERSION \  
build-date=$BUILD_DATE \  
vcs-ref=$VCS_REF \  
vcs-url=$VCS_URL \  
license="MIT"  

