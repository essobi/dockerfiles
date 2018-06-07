FROM haoliangseiue/php-cli:latest  
  
ENV SWOOLE_VERSION=2.0.9  
RUN cd /tmp && curl -SL "https://github.com/swoole/swoole-
src/archive/v${SWOOLE_VERSION}.tar.gz" | tar xzf - \  
&& cd swoole-src-${SWOOLE_VERSION} \  
&& phpize && ./configure && make && make install \  
&& docker-php-ext-enable swoole  
  
RUN docker-php-ext-configure pcntl && docker-php-ext-install pcntl  
  
RUN rm -rf /tmp/*  
  
RUN apt-get update && apt-get install -y tcpdump  
  
#############################################################################  
RUN groupadd -r swoole && useradd -r -g swoole swoole  
  
# https://github.com/tianon/gosu/blob/master/INSTALL.md#from-debian  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
fetchDeps=' \  
ca-certificates \  
wget \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
  
#
https://github.com/krallin/tini/tree/0effd37412ba5ae7e00af0db1f36f5dbc1671df9#signed-
binaries  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc
/usr/local/bin/tini.asc  
RUN gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
&& gpg --verify /usr/local/bin/tini.asc  
RUN rm /usr/local/bin/tini.asc && chmod +x /usr/local/bin/tini  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

