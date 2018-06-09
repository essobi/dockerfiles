FROM sumpfgottheit/centos7  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
# Install Supervisor and Java  
RUN yum -y install supervisor java-1.8.0-openjdk-headless  
  
#  
# INSTALL Elasticsearch, Logstash and Kibana  
#  
# Install Logstash (from https://registry.hub.docker.com/u/pblittle/docker-
logstash/dockerfile/)  
ENV LS=logstash-1.5.1  
RUN cd /tmp && \  
wget https://download.elasticsearch.org/logstash/logstash/${LS}.tar.gz && \  
echo "526bf554d1f1e27354f3816c1a3576a83ac1ca05 ${LS}.tar.gz" > sha1sum.txt &&
\  
sha1sum -c sha1sum.txt && rm sha1sum.txt && \  
tar xzvf ${LS}.tar.gz && \  
mv ${LS} /opt/logstash && \  
chown -R root:root /opt/logstash && \  
rm ${LS}.tar.gz  
# Copy minimal.conf to bin dir, so it can be taken if nothing is in the conf-
dir  
ADD logstash_minimal.conf /opt/logstash/_minimal.conf  
# Copy adapted Startscript into Container.  
COPY logstash.startscript /opt/logstash/bin/logstash  
RUN chmod 0755 /opt/logstash/bin/logstash  
  
# Install Elasticsearch  
ENV ES=elasticsearch-1.6.0  
RUN cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/${ES}.tar.gz &&
\  
echo "cb8522f5d3daf03ef96ed533d027c0e3d494e34b ${ES}.tar.gz" > sha1sum.txt &&
\  
sha1sum -c sha1sum.txt && rm sha1sum.txt && \  
tar xvfz ${ES}.tar.gz && \  
mv ${ES} /opt/elasticsearch && \  
rm ${ES}.tar.gz  
  
# Install Kibana  
ENV KIBANA=kibana-4.1.0-linux-x64  
RUN cd /tmp && \  
wget https://download.elasticsearch.org/kibana/kibana/${KIBANA}.tar.gz && \  
echo "db27d030fe0f103d416cd9acad42c35a1418b5f5 ${KIBANA}.tar.gz" > sha1sum.txt
&& \  
sha1sum -c sha1sum.txt && rm sha1sum.txt && \  
tar xvfz ${KIBANA}.tar.gz && \  
mv ${KIBANA} /opt/kibana && \  
chown -R root:root /opt/kibana && \  
rm -f ${KIBANA}.tar.gz  
  
#  
# Building the Configuration for Elasticsearch, Logstash an Kibana  
#  
# Logstash  
ENV LOGSTASH_CONF_DIR=/etc/logstash.d/  
RUN mkdir -p /etc/logstash.d/patterns  
ADD logstash_minimal.conf $LOGSTASH_CONF_DIR/_minimal.conf  
  
# Elasticsearch  
ENV ELASTICSEARCH_DATA_DIR=/var/elasticsearch  
RUN mkdir -p $ELASTICSEARCH_DATA_DIR  
  
# Copy the supervisord to the container  
COPY supervisor/*.ini /etc/supervisord.d/  
  
# Expose the Kibana Port  
EXPOSE 5601  
# Clean everything that yum left behind  
RUN yum -y clean all  
  
VOLUME ["/var/log", "/var/elasticsearch"]  
  
CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf" ]  
  

