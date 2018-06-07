FROM java:7-jre  
  
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
  
# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-
repositories.html  
# https://packages.elasticsearch.org/GPG-KEY-elasticsearch  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV ELASTICSEARCH_VERSION 0.90.5  
RUN echo "deb
http://packages.elasticsearch.org/elasticsearch/${ELASTICSEARCH_VERSION%.*}/debian
stable main" > /etc/apt/sources.list.d/elasticsearch.list  
  
RUN apt-get update \  
&& apt-get install elasticsearch=$ELASTICSEARCH_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
COPY config /usr/share/elasticsearch/config  
  
VOLUME /usr/share/elasticsearch/data  
  
COPY docker-entrypoint.sh /  
COPY docker-entrypoint-ecs.sh /  
  
WORKDIR /usr/share/elasticsearch  
RUN bin/plugin install elasticsearch/elasticsearch-cloud-aws/1.16.0  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch"]  

