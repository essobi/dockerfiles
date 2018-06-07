FROM infoexpress/java-base  
  
MAINTAINER InfoExpress  
  
ENV ES_PKG_NAME elasticsearch-1.7.2  
# Install Elasticsearch.  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
# Install head plugin  
RUN \  
cd /elasticsearch && \  
bin/plugin -i mobz/elasticsearch-head  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
ADD ./data /data  
  
# Define mountable directories.  
VOLUME ["/elasticsearch/config", "/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  
#  
# Expose ports.  
# - 9200: HTTP  
# - 9300: Transport  
EXPOSE 9200  
EXPOSE 9300  

