FROM java:8-jre  
  
# credits goes to Geoff Bourne.  
# Checkout his original repo: https://hub.docker.com/r/itzg/elasticsearch/  
MAINTAINER nicolaihald  
  
ENV ES_VERSION 2.3.2  
RUN wget -qO /tmp/es.tgz
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ES_VERSION/elasticsearch-$ES_VERSION.tar.gz
&& \  
cd /usr/share && \  
tar xf /tmp/es.tgz && \  
rm /tmp/es.tgz  
  
ENV ES_HOME /usr/share/elasticsearch-$ES_VERSION  
RUN useradd -d $ES_HOME -M -r elasticsearch && \  
chown -R elasticsearch: $ES_HOME  
  
RUN mkdir /es /es/data /es/config && touch /es/data/.CREATED
/es/config/.CREATED && chown -R elasticsearch: /es/data /es/config  
  
# Add mounting points  
VOLUME ["/es/data", "/es/config"]  
COPY config/ /es/config  
  
ADD start.sh /start.sh  
  
WORKDIR $ES_HOME  
USER elasticsearch  
  
EXPOSE 9200 9300  
# DEFAULT SETTINGS:  
ENV CLUSTER_NAME=Elastic \  
NODE_MASTER=true \  
NODE_DATA=true \  
NETWORK_HOST=_non_loopback_ \  
NETWORK_BIND_HOST=0.0.0.0 \  
  
# Set ES_HEAP_SIZE to 50% of mem_limit:  
ES_HEAP_SIZE=1g  
#ES_DISOVERY_ZEN_PING_MULTICAST_ENABLED=true \  
#ES_DISOVERY_ZEN_PING_UNICAST_HOSTS=  
# Pre-install default plugin  
#ENV PLUGINS royrusso/elasticsearch-HQ  
#ENV OPTS=-Dnetwork.host=_non_loopback_  
RUN bin/plugin install royrusso/elasticsearch-HQ  
  
CMD ["/bin/bash", "/start.sh"]

