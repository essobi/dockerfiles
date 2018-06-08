FROM debian:jessie  
  
# ENVs  
ENV GOSU_VERSION 1.10  
ENV TINI_VERSION v0.9.0  
# RUNs  
RUN groupadd -r kibana && useradd -r -m -g kibana kibana  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https ca-certificates wget libfontconfig libfreetype6 --no-
install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
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
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
RUN set -x \  
&& wget -O /usr/local/bin/tini
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" \  
&& wget -O /usr/local/bin/tini.asc
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
&& gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini \  
&& tini -h  
  
RUN set -ex; \  
key='46095ACC8548582C1A2699A9D27D666CD88E42B4'; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
gpg --export "$key" > /etc/apt/trusted.gpg.d/elastic.gpg; \  
rm -rf "$GNUPGHOME"; \  
apt-key list  
  
RUN echo 'deb https://artifacts.elastic.co/packages/6.x-prerelease/apt stable
main' > /etc/apt/sources.list.d/kibana.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends kibana \  
&& rm -rf /var/lib/apt/lists/*  
  
# Update PATH ENV  
ENV PATH /usr/share/kibana/bin:$PATH  
  
# Deploy Kibana EntryPoint and Config.  
COPY kibana.yml /kibana/kibana.yml  
COPY entrypoint.sh /  
  
EXPOSE 5601  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["kibana"]  

