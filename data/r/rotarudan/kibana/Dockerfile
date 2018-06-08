FROM debian:jessie  
  
# add our user and group first to make sure their IDs get assigned
consistently  
RUN groupadd -r kibana && useradd -r -m -g kibana kibana  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
wget \  
curl \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
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
  
# grab tini for signal processing and zombie killing  
ENV TINI_VERSION v0.9.0  
RUN set -x \  
&& wget -O /usr/local/bin/tini
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" \  
&& wget -O /usr/local/bin/tini.asc
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
&& gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \  
&& rm -r "$GNUPGHOME" /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini \  
&& tini -h  
  
# https://www.elastic.co/guide/en/kibana/4.4/setup.html#kibana-apt  
# https://packages.elasticsearch.org/GPG-KEY-elasticsearch  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV KIBANA_MAJOR 5.0  
ENV KIBANA_VERSION 5.0.0-alpha3  
  
#RUN echo "deb http://packages.elastic.co/kibana/${KIBANA_MAJOR}/debian stable
main" > /etc/apt/sources.list.d/kibana.list  
RUN echo 'deb http://packages.elastic.co/kibana/5.0.0-alpha/debian stable
main' > /etc/apt/sources.list.d/kibana.list  
# TODO figure out what's going on here and what it'll settle to for 5.0 GA  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends kibana=$KIBANA_VERSION \  
&& chown -R kibana:kibana /opt/kibana \  
&& rm -rf /var/lib/apt/lists/* \  
\  
# ensure the default configuration is useful when using --link  
&& sed -ri "s!^(\\#\s*)?(elasticsearch\\.url:).*!\2
'http://elasticsearch:9200'!" /opt/kibana/config/kibana.yml \  
&& grep -q 'elasticsearch:9200' /opt/kibana/config/kibana.yml  
  
ENV PATH /opt/kibana/bin:$PATH  
  
COPY docker-entrypoint.sh /  
COPY signup-app.js /  
COPY kibana-routes.js /  
  
# NODEJS  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 4.4.5  
RUN buildDeps='xz-utils' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& apt-get purge -y --auto-remove $buildDeps  
  
EXPOSE 5601  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["kibana"]  

