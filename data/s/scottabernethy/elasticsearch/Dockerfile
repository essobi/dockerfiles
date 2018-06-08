# Dockerfiler for scottabernethy/elasticsearch  
FROM scottabernethy/java:8  
ENV ELASTICSEARCH_VERSION 1.5.1  
RUN \  
apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4 && \  
echo "deb
http://packages.elasticsearch.org/elasticsearch/${ELASTICSEARCH_VERSION%.*}/debian
stable main" > /etc/apt/sources.list.d/elasticsearch.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
elasticsearch=$ELASTICSEARCH_VERSION \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
COPY config /usr/share/elasticsearch/config  
  
VOLUME /usr/share/elasticsearch/data  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch"]  

