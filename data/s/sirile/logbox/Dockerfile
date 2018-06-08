FROM progrium/busybox  
MAINTAINER Ilkka Anttonen version: 0.1  
# As we're not using basebox, some linking is necessary  
RUN ln -s /opt/files/java/jre/bin/java /usr/bin/java  
RUN ln -s /opt/files/runsv /sbin/runsv  
RUN ln -s /opt/files/runsvdir /sbin/runsvdir  
  
# Install Elasticsearch  
RUN ( wget
http://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.tar.gz
-O /tmp/elasticsearch.tar.gz && gunzip /tmp/elasticsearch.tar.gz && cd /opt &&
tar xf /tmp/elasticsearch.tar && rm /tmp/elasticsearch.tar)  
  
# Install Logstash  
RUN ( wget
http://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz -O
/tmp/logstash.tar.gz && gunzip /tmp/logstash.tar.gz && cd /opt && tar xf
/tmp/logstash.tar && rm /tmp/logstash.tar )  
  
# Set the scripts in place  
COPY elasticsearch /etc/service/elasticsearch/run  
COPY logstash /etc/service/logstash/run  
COPY logstash-syslog.json /opt/logstash-1.4.2/logstash-syslog.json  
  
# Expose the ports  
EXPOSE 5000 9200  
# Start runit  
CMD ["/sbin/runsvdir", "/etc/service"]  

