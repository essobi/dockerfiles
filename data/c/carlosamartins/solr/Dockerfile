FROM andreptb/oracle-java:8  
ENV SOLR_VERSION 4.4.0  
ENV SOLR solr-$SOLR_VERSION  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install lsof groovy2 && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr  
  
EXPOSE 8983  
WORKDIR /opt/solr  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]

