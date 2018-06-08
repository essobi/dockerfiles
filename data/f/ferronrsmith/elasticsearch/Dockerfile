FROM iron/java:1.8  
MAINTAINER Ferron Hanse <ferronrsmith@gmail.com>  
  
ENV ELASTICSEARCH_MAJOR 2.3  
ENV ELASTICSEARCH_VERSION 2.3.2  
ENV ELASTICSEARCH_URL_BASE
https://download.elasticsearch.org/elasticsearch/elasticsearch  
ENV PATH /opt/elasticsearch/bin:$PATH  
  
RUN set -ex \  
&& apk --update add bash curl \  
&& rm -rf /var/cache/apk/*  
RUN curl -fsSL -o /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 \  
&& chmod 0755 /usr/bin/dumb-init  
RUN set -x \  
&& curl -fsSL -o /usr/local/bin/gosu
https://github.com/tianon/gosu/releases/download/1.8/gosu-amd64 \  
&& chmod +x /usr/local/bin/gosu  
RUN set -ex \  
&& mkdir -p /opt \  
&& curl -fsSL -o /tmp/elasticsearch.tar.gz
$ELASTICSEARCH_URL_BASE/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz \  
&& tar -xzf /tmp/elasticsearch.tar.gz -C /opt \  
&& rm -f /tmp/elasticsearch.tar.gz \  
&& mv /opt/elasticsearch-$ELASTICSEARCH_VERSION /opt/elasticsearch \  
&& for path in \  
/opt/elasticsearch/data \  
/opt/elasticsearch/logs \  
/opt/elasticsearch/config \  
/opt/elasticsearch/config/scripts; do mkdir -p "$path"; done \  
&& addgroup elasticsearch \  
&& adduser -D -G elasticsearch -h /opt/elasticsearch elasticsearch \  
&& chown -R elasticsearch:elasticsearch /opt/elasticsearch  
  
COPY config /opt/elasticsearch/config  
  
VOLUME /opt/elasticsearch/data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch"]

