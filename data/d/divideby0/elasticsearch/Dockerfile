FROM clifton/oracle-java8  
MAINTAINER Cedric Hurst <cedric@spantree.net>  
  
ENV ES_PKG_NAME elasticsearch-1.4.2  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
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
  
# Install some plugins we like  
RUN /elasticsearch/bin/plugin -i lmenezes/elasticsearch-kopf/1.4.3  
  
RUN /elasticsearch/bin/plugin -i elasticsearch/marvel/latest  
  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300

