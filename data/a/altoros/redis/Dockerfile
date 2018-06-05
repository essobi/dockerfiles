FROM debian:wheezy  
  
#  
# Comment out this directive because we run the service as the vcap user  
#  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
#RUN groupadd -r redis && useradd -r -g redis redis  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
#  
# Gosu is used to change the user to `redis` but we don't need to  
#  
# grab gosu for easy step-down from root  
#RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
#RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
# && curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
# && gpg --verify /usr/local/bin/gosu.asc \  
# && rm /usr/local/bin/gosu.asc \  
# && chmod +x /usr/local/bin/gosu  
ENV REDIS_VERSION 3.0.0  
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.0.0.tar.gz  
ENV REDIS_DOWNLOAD_SHA1 c75fd32900187a7c9f9d07c412ea3b3315691c65  
  
# for redis-sentinel see: http://redis.io/topics/sentinel  
RUN buildDeps='gcc libc6-dev make'; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/redis \  
&& curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \  
&& rm redis.tar.gz \  
&& make -C /usr/src/redis \  
&& make -C /usr/src/redis install \  
&& rm -r /usr/src/redis \  
&& apt-get purge -y --auto-remove $buildDeps  
  
#  
# No need in chowning it for the vcap user  
#  
#RUN mkdir /data && chown redis:redis /data  
RUN mkdir /data  
VOLUME /data  
WORKDIR /data  
  
COPY docker-entrypoint.sh /home/vcap/entrypoint.sh  
ENTRYPOINT ["/home/vcap/entrypoint.sh"]  
  
#  
# This directive is left here for the local debug purposes only  
#  
EXPOSE 8080  
CMD [ "redis-server", "--port", "8080", "--bind", "0.0.0.0" ]  

