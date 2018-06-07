FROM holmes/java:1.7.0_71  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
ENV ES_PKG_NAME elasticsearch-1.4.2  
ENV AWS_PLUGIN_VERSION 2.4.1  
ENV KOPF_PLUGIN_VERSION 1.4.3  
RUN yum install -y tar wget  
  
# Install ElasticSearch.  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
#AWS plugin  
RUN /elasticsearch/bin/plugin install elasticsearch/elasticsearch-cloud-
aws/$AWS_PLUGIN_VERSION  
  
#Kopf plugin  
RUN /elasticsearch/bin/plugin --install lmenezes/elasticsearch-
kopf/$KOPF_PLUGIN_VERSION  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300

