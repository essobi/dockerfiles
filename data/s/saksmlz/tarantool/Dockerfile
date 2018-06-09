FROM debian:stable  
MAINTAINER mail@racktear.com  
  
RUN groupadd -r tarantool && useradd -r -g tarantool tarantool  
  
ENV GOSU_VERSION 1.7  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
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
&& gosu nobody true \  
&& apt-get purge -y ca-certificates wget \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TARANTOOL_VERSION=1.7.4-0-g927bd9c24 \  
TARANTOOL_DOWNLOAD_URL=https://github.com/tarantool/tarantool.git \  
TARANTOOL_INSTALL_LUADIR=/usr/local/share/tarantool \  
LUAROCKS_URL=http://keplerproject.github.io/luarocks/releases/luarocks-2.3.0.tar.gz
\  
LUAROCK_AVRO_SCHEMA_REPO=https://github.com/tarantool/avro-schema.git \  
LUAROCK_AVRO_SCHEMA_TAG=b49efa8 \  
LUAROCK_EXPIRATIOND_REPO=https://github.com/tarantool/expirationd.git \  
LUAROCK_EXPIRATIOND_TAG=9ec22b6 \  
LUAROCK_QUEUE_REPO=https://github.com/tarantool/queue.git \  
LUAROCK_QUEUE_TAG=24d730c \  
LUAROCK_CONNPOOL_REPO=https://github.com/tarantool/connpool.git \  
LUAROCK_CONNPOOL_TAG=685af44 \  
LUAROCK_SHARD_REPO=https://github.com/tarantool/shard.git \  
LUAROCK_SHARD_TAG=278b906 \  
LUAROCK_HTTP_REPO=https://github.com/tarantool/http.git \  
LUAROCK_HTTP_TAG=4486de9 \  
LUAROCK_TARANTOOL_PROMETHEUS_REPO=https://github.com/tarantool/prometheus.git
\  
LUAROCK_TARANTOOL_PROMETHEUS_TAG=0654304 \  
LUAROCK_TARANTOOL_CURL_REPO=https://github.com/tarantool/curl.git \  
LUAROCK_TARANTOOL_CURL_TAG=2.2.7  
  
COPY luarocks-config.lua /usr/local/etc/luarocks/config-5.1.lua  
  
RUN \  
BUILD_PACKAGES=' \  
devscripts \  
equivs \  
git \  
build-essential \  
ca-certificates \  
wget \  
make \  
cmake \  
cdbs \  
gcc \  
g++ \  
unzip \  
libreadline-dev \  
libncurses5-dev \  
binutils-dev \  
libiberty-dev \  
libbfd-dev \  
uuid-dev \  
liblua5.1-0-dev \  
libev-dev \  
libcurl4-openssl-dev'; \  
set -ex \  
&& apt-get update \  
&& apt-get upgrade --yes \  
&& apt-get install --yes --no-install-recommends \  
$BUILD_PACKAGES \  
lua5.1 \  
libyaml-dev \  
libssl-dev \  
libgomp1 \  
libev4 \  
&& : "---------- tarantool ----------" \  
&& mkdir -p /usr/src/tarantool \  
&& git clone "$TARANTOOL_DOWNLOAD_URL" /usr/src/tarantool \  
&& git -C /usr/src/tarantool checkout "$TARANTOOL_VERSION" \  
&& git -C /usr/src/tarantool submodule update --init --recursive \  
&& (cd /usr/src/tarantool; \  
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo\  
-DENABLE_BUNDLED_LIBYAML:BOOL=OFF\  
-DENABLE_BACKTRACE:BOOL=ON\  
-DENABLE_DIST:BOOL=ON\  
.) \  
&& make -C /usr/src/tarantool -j\  
&& make -C /usr/src/tarantool install \  
&& make -C /usr/src/tarantool clean \  
&& : "---------- small ----------" \  
&& (cd /usr/src/tarantool/src/lib/small; \  
cmake -DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_INSTALL_LIBDIR=lib \  
-DCMAKE_BUILD_TYPE=RelWithDebInfo \  
.) \  
&& make -C /usr/src/tarantool/src/lib/small \  
&& make -C /usr/src/tarantool/src/lib/small install \  
&& make -C /usr/src/tarantool/src/lib/small clean \  
&& : "---------- msgpuck ----------" \  
&& (cd /usr/src/tarantool/src/lib/msgpuck; \  
cmake -DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_INSTALL_LIBDIR=lib \  
-DCMAKE_BUILD_TYPE=RelWithDebInfo \  
.) \  
&& make -C /usr/src/tarantool/src/lib/msgpuck \  
&& make -C /usr/src/tarantool/src/lib/msgpuck install \  
&& make -C /usr/src/tarantool/src/lib/msgpuck clean \  
&& : "---------- luarocks ----------" \  
&& wget -O luarocks.tar.gz "$LUAROCKS_URL" \  
&& mkdir -p /usr/src/luarocks \  
&& tar -xzf luarocks.tar.gz -C /usr/src/luarocks --strip-components=1 \  
&& (cd /usr/src/luarocks; \  
./configure; \  
make build; \  
make install) \  
&& rm -r /usr/src/luarocks \  
&& rm -rf /usr/src/tarantool \  
&& mkdir -p /rocks \  
&& luarocks install lua-term \  
&& : "avro" \  
&& git clone $LUAROCK_AVRO_SCHEMA_REPO /rocks/avro \  
&& git -C /rocks/avro checkout $LUAROCK_AVRO_SCHEMA_TAG \  
&& (cd /rocks/avro && luarocks make *rockspec) \  
&& : "expirationd" \  
&& git clone $LUAROCK_EXPIRATIOND_REPO /rocks/expirationd \  
&& git -C /rocks/expirationd checkout $LUAROCK_EXPIRATIOND_TAG \  
&& (cd /rocks/expirationd && luarocks make *rockspec) \  
&& : "queue" \  
&& git clone $LUAROCK_QUEUE_REPO /rocks/queue \  
&& git -C /rocks/queue checkout $LUAROCK_QUEUE_TAG \  
&& (cd /rocks/queue && luarocks make *rockspec) \  
&& : "connpool" \  
&& git clone $LUAROCK_CONNPOOL_REPO /rocks/connpool \  
&& git -C /rocks/connpool checkout $LUAROCK_CONNPOOL_TAG \  
&& (cd /rocks/connpool && luarocks make *rockspec) \  
&& : "shard" \  
&& git clone $LUAROCK_SHARD_REPO /rocks/shard \  
&& git -C /rocks/shard checkout $LUAROCK_SHARD_TAG \  
&& (cd /rocks/shard && luarocks make *rockspec) \  
&& : "http" \  
&& git clone $LUAROCK_HTTP_REPO /rocks/http \  
&& git -C /rocks/http checkout $LUAROCK_HTTP_TAG \  
&& (cd /rocks/http && luarocks make *rockspec) \  
&& : "prometheus" \  
&& git clone $LUAROCK_TARANTOOL_PROMETHEUS_REPO /rocks/prometheus \  
&& git -C /rocks/prometheus checkout $LUAROCK_TARANTOOL_PROMETHEUS_TAG \  
&& (cd /rocks/prometheus && luarocks make *rockspec) \  
&& : "curl" \  
&& git clone $LUAROCK_TARANTOOL_CURL_REPO /rocks/curl \  
&& git -C /rocks/curl checkout $LUAROCK_TARANTOOL_CURL_TAG \  
&& (cd /rocks/curl && luarocks make *rockspec) \  
&& : "---------- remove build deps ----------" \  
&& apt-get purge -y $BUILD_PACKAGES \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/lib/tarantool \  
&& chown tarantool:tarantool /var/lib/tarantool \  
&& mkdir -p /opt/tarantool \  
&& chown tarantool:tarantool /opt/tarantool \  
&& mkdir -p /var/run/tarantool \  
&& chown tarantool:tarantool /var/run/tarantool \  
&& mkdir /etc/tarantool \  
&& chown tarantool:tarantool /etc/tarantool  
  
VOLUME /var/lib/tarantool  
WORKDIR /opt/tarantool  
  
COPY tarantool-entrypoint.lua /usr/local/bin/  
COPY tarantool_set_config.lua /usr/local/bin/  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY console /usr/local/bin/  
COPY tarantool_is_up /usr/local/bin/  
COPY tarantool.default /usr/local/etc/default/tarantool  
  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3301  
CMD [ "tarantool" ]  

