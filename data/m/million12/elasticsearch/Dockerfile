FROM centos:centos7  
MAINTAINER Marcin Ryzycki marcin@m12.io, Przemyslaw Ozgo linux@ozgo.info  
  
ENV ELASTICSEARCH_VERSION 1.7.1  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y tar java-1.7.0-openjdk && \  
yum clean all && \  
mkdir -p /opt/elasticsearch && \  
cd /opt/elasticsearch && \  
curl -O
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz
&& \  
tar zxvf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz -C /opt/elasticsearch
--strip-components=1 && \  
rm -f elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz && \  
/opt/elasticsearch/bin/plugin -i elasticsearch/marvel/latest  
  
CMD /opt/elasticsearch/bin/elasticsearch  
  
EXPOSE 9200  

