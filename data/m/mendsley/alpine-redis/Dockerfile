FROM mendsley/alpine-gosu  
MAINTAINER Matthew Endsley <mendsley@gmail.com>  
  
# add our user/group first to ensure my get consistent ids  
RUN addgroup redis \  
&& adduser -H -D -s /bin/false -G redis redis  
  
# Patches for Alpine compatibility \  
ENV REDIS_VERSION="3.2.9" \  
REDIS_DOWNLOAD_URL="http://download.redis.io/releases/redis-3.2.9.tar.gz" \  
REDIS_DOWNLOAD_SHA1="8fad759f28bcb14b94254124d824f1f3ed7b6aa6"  
# Download and build redis  
RUN buildDeps='curl tar patch make gcc musl-dev linux-headers' \  
&& set -x \  
&& apk add --update $buildDeps \  
&& curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/redis \  
&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \  
&& rm -f redis.tar.gz \  
&& cd /usr/src/redis \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src \  
&& apk del $buildDeps \  
&& rm -rf /var/cache/apk/* \  
;  
  
RUN mkdir /data \  
&& chown redis:redis /data \  
;  
VOLUME /data  
WORKDIR /data  
  
COPY docker-entry-point.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 6379  
CMD ["redis-server"]  

