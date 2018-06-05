FROM cloudbees/java-build-tools:1.0.0  
USER root  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r redis && useradd -r -g redis redis  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
ENV REDIS_VERSION 3.0.7  
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.0.7.tar.gz  
ENV REDIS_DOWNLOAD_SHA1 e56b4b7e033ae8dbf311f9191cf6fdf3ae974d1c  
  
# for redis-sentinel see: http://redis.io/topics/sentinel  
RUN buildDeps='gcc libc6-dev make' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL" \  
&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \  
&& mkdir -p /usr/src/redis \  
&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \  
&& rm redis.tar.gz \  
&& make -C /usr/src/redis \  
&& make -C /usr/src/redis install \  
&& rm -r /usr/src/redis \  
&& apt-get purge -y --auto-remove $buildDeps  
  
# Install Ruby.  
RUN \  
apt-get update && \  
apt-get install -y ruby ruby-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install license_finder  
  
RUN mkdir /data && chown redis:redis /data  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 6379  
COPY redis-server-start.sh /redis-server-start.sh  
  
# Install JQ  
RUN apt-get update && apt-get install jq  
  
# Install latest CF CLI  
RUN \  
rm /usr/local/bin/cf \  
&& wget -q -O -
https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key
add - \  
&& echo "deb http://packages.cloudfoundry.org/debian stable main" >
/etc/apt/sources.list.d/cloudfoundry-cli.list \  
&& apt-get update \  
&& apt-get install cf-cli \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

