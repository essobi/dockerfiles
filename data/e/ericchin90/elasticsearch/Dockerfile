# VERSION 0.0.1  
# BUILD-USING: docker build -t ericchin90/elasticsearch .  
# PUSH-USING: docker push ericchin90/elasticsearch  
FROM ericchin90/jdk7  
MAINTAINER Eric Chin <ericchin90@gmail.com>  
  
WORKDIR /opt  
  
RUN wget -q -O elasticsearch.tar.gz
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.tar.gz
\  
&& tar -zxf elasticsearch.tar.gz \  
&& mv elasticsearch-1.3.4 elasticsearch \  
&& rm elasticsearch.tar.gz  
  
RUN sed -i "/cluster.name:/c\cluster.name: LiferayElasticSearch"
/opt/elasticsearch/config/elasticsearch.yml \  
&& echo 'http.cors.enabled: true' >>
/opt/elasticsearch/config/elasticsearch.yml  
  
ENV ES_HEAP_SIZE 2g  
  
CMD ["/opt/elasticsearch/bin/elasticsearch"]  

