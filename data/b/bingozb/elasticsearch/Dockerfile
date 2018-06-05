# https://github.com/elastic/elasticsearch-docker  
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.2  
MAINTAINER bingo <bingov5@icloud.com>  
  
ENV ES_JAVA_OPTS "-Xmx256m -Xms256m"  
ADD https://raw.githubusercontent.com/bingozb/docker-
elasticsearch/master/elasticsearch.yml
/usr/share/elasticsearch/config/elasticsearch.yml  
  
USER root  
  
RUN chown -R elasticsearch:root /usr/share/elasticsearch/config && cat
/usr/share/elasticsearch/config/elasticsearch.yml  
  
USER elasticsearch  
  
EXPOSE 9200 9300

