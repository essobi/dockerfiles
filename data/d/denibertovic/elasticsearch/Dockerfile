# Elasticsearch  
#  
# distributed restful search and analytics  
#  
# VERSION 1.4.4  
FROM debian:jessie  
MAINTAINER Deni Bertovic "me@denibertovic.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y ca-certificates wget openjdk-7-jre  
RUN wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.4.tar.gz
-O /tmp/elasticsearch.tar.gz 2> /dev/null  
  
RUN tar zxvf /tmp/elasticsearch.tar.gz -C /opt  
RUN mv /opt/elasticsearch-1.4.4 /opt/elasticsearch  
RUN rm -rf /tmp/elasticsearch.tar.gz  
  
ADD start_elasticsearch.sh /usr/local/bin/start_elasticsearch.sh  
RUN chmod +x /usr/local/bin/start_elasticsearch.sh  
  
VOLUME ["/opt/elasticsearch/config", "/opt/elasticsearch/data",
"/opt/elasticsearch/logs"]  
  
EXPOSE 9200  
EXPOSE 9300  
CMD /usr/local/bin/start_elasticsearch.sh  
  

