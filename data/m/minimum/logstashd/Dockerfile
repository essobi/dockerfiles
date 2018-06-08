FROM minimum/oracle-java:8  
MAINTAINER minimum@cepave.com  
  
# Install Logstash  
RUN \  
apt-get install -y wget && \  
(wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | \  
apt-key add -) && \  
(echo "deb http://packages.elasticsearch.org/logstash/1.5/debian stable main"
| \  
tee -a /etc/apt/sources.list) && \  
apt-get update && \  
apt-get install -y logstash  
  
# Copy SSL certificate  
COPY ./certs/* /certs/  
  
# Copy prepared Logstash configurations  
COPY ./conf.d/*.conf /etc/logstash/conf.d/  
  
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
EXPOSE 5043  
# Run Elasticsearch Service  
CMD ["/usr/bin/supervisord"]  

