FROM cpelka/java:jdk7-mvn3.3-git  
  
MAINTAINER Carsten Pelka <carsten.pelka@gmail.com>  
  
# Configuration: Cassandra Version & Plugin Version  
ENV CASSANDRA_VERSION 2.1.8  
ENV PLUGIN_VERSION $CASSANDRA_VERSION.0  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
514A2AD631A57A16DD0047EC749D6EEC0353B12C  
  
RUN echo 'deb http://www.apache.org/dist/cassandra/debian 21x main' >>
/etc/apt/sources.list.d/cassandra.list  
  
RUN apt-get update \  
&& apt-get install -y cassandra="$CASSANDRA_VERSION" \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CASSANDRA_CONFIG /etc/cassandra  
  
# listen to all rpc  
RUN sed -ri ' \  
s/^(rpc_address:).*/\1 0.0.0.0/; \  
' "$CASSANDRA_CONFIG/cassandra.yaml"  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Lucene Plugin  
RUN cd /tmp/ \  
&& git clone https://github.com/Stratio/cassandra-lucene-index \  
&& cd cassandra-lucene-index \  
&& git checkout $PLUGIN_VERSION \  
&& mvn clean package \  
&& cp plugin/target/cassandra-lucene-index-plugin-$PLUGIN_VERSION.jar
/usr/share/cassandra/lib/  
  
VOLUME /var/lib/cassandra/data  
  
EXPOSE 9042  
CMD ["cassandra", "-f"]  
  

