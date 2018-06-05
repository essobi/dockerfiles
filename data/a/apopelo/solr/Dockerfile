FROM java:8  
MAINTAINER Andrey Popelo andrey@popelo.com  
  
ENV SOLR_VERSION 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install \  
curl \  
lsof \  
procps && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
mv /opt/$SOLR /opt/solr  
  
EXPOSE 8983  
WORKDIR /opt/solr  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]  

