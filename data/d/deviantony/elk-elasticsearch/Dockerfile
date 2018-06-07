FROM java:7  
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add - && \  
echo "deb http://packages.elasticsearch.org/elasticsearch/1.5/debian stable
main" | tee -a /etc/apt/sources.list.d/elasticsearch.list && \  
apt-get update && apt-get install elasticsearch && \  
mkdir -p /usr/share/elasticsearch/config && \  
ln -s /etc/elasticsearch/elasticsearch.yml
/usr/share/elasticsearch/config/elasticsearch.yml && \  
ln -s /etc/elasticsearch/logging.yml
/usr/share/elasticsearch/config/logging.yml  
  
VOLUME ["/var/lib/elasticsearch"]  
VOLUME ["/usr/share/elasticsearch/data/"]  
  
ADD conf/elasticsearch.default /etc/default/elasticsearch  
ADD conf/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
  
EXPOSE 9200  
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/marvel/latest  
  
ENTRYPOINT ["/usr/share/elasticsearch/bin/elasticsearch"]  

