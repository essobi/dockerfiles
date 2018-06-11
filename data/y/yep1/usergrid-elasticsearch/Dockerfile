#  
# Elasticsearch Dockerfile for Usergrid  
#  
# https://github.com/yep/usergrid-elasticsearch  
#  
FROM yep1/usergrid-java  
  
ENV ES_PKG_NAME elasticsearch-1.7.4  
# install elasticsearch  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
# define mountable directories  
VOLUME ["/data"]  
  
# default command  
CMD ["/elasticsearch/bin/elasticsearch"]  
  
# expose ports  
# - 9200: HTTP  
# - 9300: native transport  
EXPOSE 9200  
EXPOSE 9300  
# config  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  

