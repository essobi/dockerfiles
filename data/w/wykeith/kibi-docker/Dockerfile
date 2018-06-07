FROM debian:jessie  
  
RUN groupadd -r kibi && useradd -r -m -g kibi kibi  
  
RUN apt-get update \  
&& apt-get clean \  
&& apt-get install -y wget unzip ca-certificates --no-install-recommends  
  
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
  
RUN cd /opt \  
&& wget
https://github.com/sirensolutions/kibi/releases/download/tag-4.5.4/kibi-
community-standalone-4.5.4-linux-x64.zip \  
&& unzip kibi-community-standalone-4.5.4-linux-x64.zip \  
&& ln -s kibi-community-standalone-4.5.4-linux-x64 kibi \  
&& chown -R kibi:kibi /opt  
  
COPY entrypoint.sh /opt/  
ENV PATH /opt/kibi/bin:$PATH  
  
RUN chmod 755 /opt/entrypoint.sh  
  
EXPOSE 5606  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["kibi"]  

