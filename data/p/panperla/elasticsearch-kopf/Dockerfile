# Elastic search with Kopf 2.0  
#  
FROM elasticsearch  
MAINTAINER maciej.perlinski@meant4.com  
ENV ES_HEAP_SIZE 2g  
EXPOSE 9200  
EXPOSE 9300  
RUN apt-get update && apt-get upgrade -y  
RUN /usr/share/elasticsearch/bin/plugin install lmenezes/elasticsearch-
kopf/2.0

