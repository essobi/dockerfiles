FROM wellsie/centos7-openjdk:1.7.0  
MAINTAINER Jono Wells <_@oj.io>  
  
# Install Elasticsearch  
COPY yum.repos.d/elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo  
RUN rpm --import http://packages.elasticsearch.org/GPG-KEY-elasticsearch \  
&& yum -y install elasticsearch-1.1.1 \  
&& yum -y clean all  
  
# Install plugins  
RUN /usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf \  
&& /usr/share/elasticsearch/bin/plugin -url
http://download.elasticsearch.org/kibana/kibana/kibana-latest.zip -install
elasticsearch/kibana3  
  
# Expose port 9200  
EXPOSE 9200  
# Start Elasticsearch  
CMD /usr/share/elasticsearch/bin/elasticsearch  

