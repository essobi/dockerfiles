FROM debian:stable  
MAINTAINER mail@racktear.com  
  
RUN groupadd -r tarantool && useradd -r -g tarantool tarantool  
  
ENV GOSU_VERSION 1.10  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
gnupg2 \  
dirmngr \  
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
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y ca-certificates wget gnupg2 dirmngr \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TARANTOOL_VERSION=1.9.0-52-g38b2a29ff \  
TARANTOOL_DOWNLOAD_URL=https://github.com/tarantool/tarantool.git \  
TARANTOOL_INSTALL_LUADIR=/usr/local/share/tarantool \  
LUAROCKS_URL=https://github.com/tarantool/luarocks/archive/6e6fe62d9409fe2103c0fd091cccb3da0451faf5.tar.gz
\  
LUAROCK_SHARD_REPO=https://github.com/tarantool/shard.git \  
LUAROCK_SHARD_TAG=8f8c5a7 \  
LUAROCK_AVRO_SCHEMA_VERSION=2.0.1 \  
LUAROCK_EXPERATIOND_VERSION=1.0.1 \  
LUAROCK_QUEUE_VERSION=1.0.2 \  
LUAROCK_CONNPOOL_VERSION=1.1.1 \  
LUAROCK_HTTP_VERSION=1.0.1 \  
LUAROCK_TARANTOOL_CURL_VERSION=2.3.1 \  
LUAROCK_TARANTOOL_PROMETHEUS_VERSION=1.0.0  
  
COPY luarocks-config.lua /usr/local/etc/luarocks/config-5.1.lua  
  
RUN \  
BUILD_PACKAGES=' \  
devscripts \  
equivs \  
git \  
build-essential \  
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
libunwind-dev \  
libicu-dev \  
libev-dev \  
libcurl4-openssl-dev'; \  
set -ex \  
&& apt-get update \  
&& apt-get upgrade --yes \  
&& apt-get install --yes --no-install-recommends $BUILD_PACKAGES ca-
certificates lua5.1 libyaml-dev libssl1.0-dev libgomp1 libicu57 libunwind8
libcurl3 libev4 \  
&& ln -sf /usr/lib/x86_64-linux-gnu/libssl.so.1.0.2 /usr/lib/x86_64-linux-
gnu/libssl.so \  
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
&& luarocks install avro-schema $LUAROCK_AVRO_SCHEMA_VERSION \  
&& : "expirationd" \  
&& luarocks install expirationd $LUAROCK_EXPERATIOND_VERSION \  
&& : "queue" \  
&& luarocks install queue $LUAROCK_QUEUE_VERSION \  
&& : "connpool" \  
&& luarocks install connpool $LUAROCK_CONNPOOL_VERSION \  
&& : "shard" \  
&& git clone $LUAROCK_SHARD_REPO /rocks/shard \  
&& git -C /rocks/shard checkout $LUAROCK_SHARD_TAG \  
&& (cd /rocks/shard && luarocks make *rockspec) \  
&& : "http" \  
&& luarocks install http $LUAROCK_HTTP_VERSION \  
&& : "prometheus" \  
&& luarocks install prometheus $LUAROCK_TARANTOOL_PROMETHEUS_VERSION \  
&& : "curl" \  
&& luarocks install tarantool-curl $LUAROCK_TARANTOOL_CURL_VERSION \  
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
COPY tarantool_is_up /usr/local/bin/  
COPY tarantool.default /usr/local/etc/default/tarantool  
  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3301  
CMD [ "tarantool" ]  

