FROM node:0.10-slim  
  
RUN groupadd -r camo && useradd -r -m -g camo camo  
  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates && rm -rf /var/lib/apt/lists/*  
  
# grab gosu for easy step-down from root  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends wget && rm -rf
/var/lib/apt/lists/* \  
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
&& apt-get purge -y --auto-remove wget  
  
# grab tini for signal processing and zombie killing  
ENV TINI_VERSION v0.9.0  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends wget && rm -rf
/var/lib/apt/lists/* \  
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
&& tini -h \  
&& apt-get purge -y --auto-remove wget  
  
ENV CAMO_VERSION 2.3.0  
ENV CAMO_DOWNLOAD_URL https://github.com/atmos/camo/archive/v2.3.0.tar.gz  
  
RUN mkdir -p /var/lib/camo \  
&& cd /var/lib/camo \  
&& npm install $CAMO_DOWNLOAD_URL \  
&& npm cache clear  
  
WORKDIR /var/lib/camo  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8081  
CMD [ "camo" ]  

