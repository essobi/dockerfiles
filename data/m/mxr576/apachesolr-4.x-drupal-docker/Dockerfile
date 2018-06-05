FROM java:openjdk-7-jdk  
  
MAINTAINER Dezső BICZÓ "mxr576@gmail.com"  
# Install some additional package.  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install git lsof supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV SOLR_VERSION 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_MEM_SIZE 512m  
ENV PARTIAL_SEARCH_ENABLED false  
  
# Download Solr.  
RUN mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
mv /opt/$SOLR /opt/solr  
  
# Add Search API Solr schema files.  
RUN git clone \--branch 7.x-1.x
http://git.drupal.org/project/search_api_solr.git && \  
mkdir -p /srv/solr/schemas/default && \  
mkdir -p /srv/solr/schemas/partial_search && \  
cp search_api_solr/solr-conf/4.x/* /srv/solr/schemas/default && \  
cp search_api_solr/solr-conf/4.x/* /srv/solr/schemas/partial_search && \  
rm -f /srv/solr/schemas/partial_search/schema.xml && \  
rm -rf ./search_api_solr* && \  
rm -rf /opt/solr/example/solr/collection1/conf  
  
# Add partial search schema.  
COPY ./partial_search/schema.xml /srv/solr/schemas/partial_search/schema.xml  
  
# Add supervisord config.  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add start script.  
COPY run.sh /run.sh  
  
# Add executable right to the file.  
RUN chmod +x /run.sh  
  
VOLUME ["/opt/solr/example/solr/collection1/data",
"/opt/solr/example/solr/collection1/conf", "/var/log/supervisor/"]  
  
EXPOSE 8983  
CMD ["/bin/bash", "-c", "/run.sh"]  

