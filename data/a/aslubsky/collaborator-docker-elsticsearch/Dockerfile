FROM java:8-jre  
  
ENV ES_VERSION 1.7.5  
# Install ElasticSearch.  
RUN \  
cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz
&& \  
tar xvzf elasticsearch-${ES_VERSION}.tar.gz && \  
rm -f elasticsearch-${ES_VERSION}.tar.gz && \  
mv /tmp/elasticsearch-${ES_VERSION} /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
EXPOSE 9200  
EXPOSE 9300  
# Elasticsearch plugins woop!  
RUN /elasticsearch/bin/plugin install elasticsearch/elasticsearch-analysis-
icu/2.7.0  
  
RUN apt-get update --fix-missing  
RUN apt-get -y install python-pip  
RUN pip install envtpl  
  
# Add etcdenv  
ADD https://github.com/upfluence/etcdenv/releases/download/v0.3.1/etcdenv-
linux-amd64-0.3.1 /usr/local/bin/etcdenv  
RUN chmod +x /usr/local/bin/etcdenv  
  
ADD elasticsearch.yml.tpl /elasticsearch/config/elasticsearch.yml.tpl  
  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
CMD run  
  

