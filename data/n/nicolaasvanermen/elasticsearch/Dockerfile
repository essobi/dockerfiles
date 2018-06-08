#  
# STYLELABS NV  
# Elasticsearch container with Head plugin  
#  
#FROM gliderlabs/alpine:3.2  
FROM sillelien/base-alpine  
MAINTAINER Fréderic Fosselle <ff@stylelabs.com>  
  
ENV PKG_NAME elasticsearch-1.5.2  
# Update and install all of the required packages  
RUN apk update && \  
apk upgrade && \  
apk add wget tar openjdk7-jre-base supervisor && \  
rm -rf /var/cache/apk/*  
  
# Install Elasticsearch and Head plugin  
RUN \  
cd / && \  
wget
http://download.elasticsearch.org/elasticsearch/elasticsearch/$PKG_NAME.tar.gz
-nv && \  
tar xvzf $PKG_NAME.tar.gz && \  
rm -f $PKG_NAME.tar.gz && \  
mv $PKG_NAME /elasticsearch && \  
elasticsearch/bin/plugin -install mobz/elasticsearch-head && \  
apk del wget tar  
  
ADD config/supervisord/supervisord.conf /etc/supervisord.conf  
ADD config/supervisord/elasticsearch.conf /etc/supervisor.d/elasticsearch.conf  
  
# Define default command  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n"]  
  
EXPOSE 9200 9300  

