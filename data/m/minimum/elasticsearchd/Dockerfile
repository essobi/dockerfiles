FROM minimum/oracle-java:8  
MAINTAINER minimum@cepave.com  
  
# Install Elasticsearch 1.6  
RUN \  
apt-get install -y wget && \  
(wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | \  
apt-key add -) && \  
(echo "deb http://packages.elastic.co/elasticsearch/1.6/debian stable main" |
\  
tee -a /etc/apt/sources.list.d/elasticsearch-1.6.list) && \  
apt-get update && \  
apt-get install -y elasticsearch && \  
update-rc.d elasticsearch defaults 95 10  
  
# Install Supervisor  
RUN \  
apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Clean  
RUN \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Port  
EXPOSE 9200 9300  
# Run Elasticsearch Service  
CMD ["/usr/bin/supervisord"]  

