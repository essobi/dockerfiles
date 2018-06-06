FROM traxair/oracle-java7:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add - && \  
echo "deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable
main" | tee -a /etc/apt/sources.list.d/elasticsearch.list && \  
apt-get update && \  
apt-get install -y elasticsearch && \  
mkdir -p /usr/share/elasticsearch/config && \  
ln -s /etc/elasticsearch/elasticsearch.yml
/usr/share/elasticsearch/config/elasticsearch.yml && \  
ln -s /etc/elasticsearch/logging.yml
/usr/share/elasticsearch/config/logging.yml && \  
/usr/share/elasticsearch/bin/plugin -i elasticsearch/marvel/latest && \  
apt-get clean && \  
apt-get purge  
  
  
  
VOLUME ["/var/lib/elasticsearch", "/usr/share/elasticsearch/data",
"/usr/share/elasticsearch/logs"]  
  
ADD conf/elasticsearch.default /etc/default/elasticsearch  
ADD conf/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
  
EXPOSE 9200  
  
ENTRYPOINT ["/usr/share/elasticsearch/bin/elasticsearch"]  

