FROM java:8-jre  
  
RUN apt-get update  
RUN apt-get install -y wget  
  
ENV ES_VERSION 1.7.1  
WORKDIR /opt  
  
RUN wget -O-
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz
| tar xfz -  
RUN mv /opt/elasticsearch-$ES_VERSION /opt/elasticsearch  
  
RUN /opt/elasticsearch/bin/plugin -i elasticsearch/license/latest  
RUN /opt/elasticsearch/bin/plugin -i elasticsearch/shield/latest  
RUN /opt/elasticsearch/bin/plugin -i elasticsearch/marvel/latest  
RUN /opt/elasticsearch/bin/plugin -i elasticsearch/watcher/latest  
  
VOLUME /data  
VOLUME /config  
  
ENV ES_JAVA_OPTS -Des.path.conf=/config  
  
WORKDIR /opt/elasticsearch/bin  
  
CMD ["/opt/elasticsearch/bin/elasticsearch"]  

