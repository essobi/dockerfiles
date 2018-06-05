############################################################  
# Dockerfile to build ElasticSearch container images  
# with support additional languages  
############################################################  
  
FROM openjdk  
  
MAINTAINER Corey Coto <corey.coto@gmail.com>  
  
ENV ES_PKG_NAME elasticsearch-2.4.3  
  
# Install Elasticsearch.  
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
  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch", "-Des.insecure.allow.root=true"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Inquisitor  
RUN /elasticsearch/bin/plugin install polyfractal/elasticsearch-inquisitor  
  
# KOPF  
RUN /elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf  
  
# ICU Analysis  
RUN /elasticsearch/bin/plugin install analysis-icu  
  
# Japanese (kuromoji) Analysis  
RUN /elasticsearch/bin/plugin install analysis-kuromoji  
  
# Smart Chinese Analysis  
RUN /elasticsearch/bin/plugin install analysis-smartcn  
  
# Polish Analysis  
RUN /elasticsearch/bin/plugin install analysis-stempel  
  
# Russian Morphological Analysis  
RUN /elasticsearch/bin/plugin install
http://dl.bintray.com/content/imotov/elasticsearch-
plugins/org/elasticsearch/elasticsearch-analysis-
morphology/2.4.3/elasticsearch-analysis-morphology-2.4.3.zip  
  
# Delete-by-query plugin  
RUN /elasticsearch/bin/plugin install delete-by-query  

