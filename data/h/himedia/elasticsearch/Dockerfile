#  
# ElasticSearch v0.90.13 Dockerfile  
#  
FROM phusion/baseimage:0.9.11  
MAINTAINER Geoffroy Aubry <gaubry@hi-media.com>  
  
# Install Java:  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java7-installer  
  
# Install ElasticSearch:  
ENV ES_VERSION 0.90.13  
RUN cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz
&& \  
tar xvzf elasticsearch-${ES_VERSION}.tar.gz && \  
rm -f elasticsearch-${ES_VERSION}.tar.gz && \  
mv /tmp/elasticsearch-${ES_VERSION} /elasticsearch  
  
# Define mountable directories:  
VOLUME ["/data"]  
  
ADD ./elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
WORKDIR /data  
  
# 9200: HTTP  
EXPOSE 9200  
# 9300: transport  
EXPOSE 9300  
# Init process:  
RUN echo "#!/bin/sh\n/elasticsearch/bin/elasticsearch" >
/etc/my_init.d/01_elasticsearch.sh  
RUN chmod +x /etc/my_init.d/01_elasticsearch.sh  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

