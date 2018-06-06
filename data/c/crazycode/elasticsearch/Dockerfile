FROM crazycode/jdk7  
  
MAINTAINER crazycode  
ENV DEBIAN_FRONTEND noninteractive  
ENV ES_PKG_NAME elasticsearch-1.4.1  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get -qq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install ElasticSearch.  
RUN \  
cd / && \  
wget
http://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Define working directory.  
WORKDIR /data  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  

