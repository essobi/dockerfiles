#  
# Elasticsearch Dockerfile  
#  
# https://github.com/dockerfile/elasticsearch  
#  
# Pull base image.  
FROM centos:centos7  
  
ENV ES_PKG_NAME elasticsearch-1.6.0  
RUN \  
yum update -y && \  
yum install -y tar wget java-1.7.0-openjdk && \  
yum install -y epel-release && \  
yum clean all  
  
# Install Kibana4  
RUN \  
mkdir -p /opt/kibana && \  
cd /opt/kibana && \  
curl -o /tmp/kibana4.tgz
https://download.elastic.co/kibana/kibana/kibana-4.1.0-linux-x64.tar.gz && \  
tar zxvf /tmp/kibana4.tgz -C /opt/kibana --strip-components=1 && \  
rm -f /tmp/kibana4.tgz  
  
ENV KIBANA_CONFIG /opt/kibana/config/kibana.yml  
  
ADD bin/bootstrap.sh /bootstrap.sh  
  
# Install Elasticsearch.  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Define working directory.  
WORKDIR /data  
  
#Install Supervisor and config  
RUN yum install --enablerepo=epel -y supervisor  
RUN touch /etc/supervisord.conf  
RUN echo '[supervisord]' >> /etc/supervisord.conf  
RUN echo 'nodaemon=true' >> /etc/supervisord.conf  
RUN echo '[program:elasticsearch]' >> /etc/supervisord.conf  
RUN echo 'command=/elasticsearch/bin/elasticsearch' >> /etc/supervisord.conf  
RUN echo '[program:kibana]' >> /etc/supervisord.conf  
RUN echo 'command=/bootstrap.sh' >> /etc/supervisord.conf  
  
EXPOSE 9200  
EXPOSE 9300  
EXPOSE 5601  
CMD /usr/bin/supervisord -c /etc/supervisord.conf  

