# This is a docker Elasticsearch environment for PNX QA and Staging.  
#  
FROM elasticsearch:1.7.3  
MAINTAINER Peter Lieverdink <peter.lieverdink@previousnext.com.au>  
  
# Only used for test builds.  
ENV ES_HEAP_SIZE 128m  
  
##  
# Configure ElasticSearch for PNX.  
##  
ADD ./conf/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
  
##  
# Repeat the ES steps.  
##  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
VOLUME /usr/share/elasticsearch/data  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch"]  

