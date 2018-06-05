# https://github.com/elastic/elasticsearch-docker  
FROM docker.elastic.co/elasticsearch/elasticsearch:5.2.2  
  
ADD config/elasticsearch.yml /usr/share/elasticsearch/config/  
  
USER root  
RUN chown elasticsearch:elasticsearch
/usr/share/elasticsearch/config/elasticsearch.yml  
RUN bin/elasticsearch-plugin install repository-s3  
  
USER elasticsearch  

