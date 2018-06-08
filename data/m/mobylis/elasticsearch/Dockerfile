FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.4  
RUN rm -f plugins/repository-gcs  
RUN bin/elasticsearch-plugin install repository-gcs --batch

