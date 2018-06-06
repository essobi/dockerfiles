FROM java:openjdk-8-jre  
MAINTAINER Lisa Ridley "lisa@prometsource.com"  
ENV SOLR_VERSION 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_USER solr  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install lsof procps && \  
groupadd -r $SOLR_USER && \  
useradd -r -g $SOLR_USER $SOLR_USER && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr && \  
## Specific for MC; this may not be necessary, but we'll leave it in for now.  
mkdir -p /opt/solr/example/solr/collection1/conf && \  
mkdir -p /usr/local/share/solr-config && \  
## end specific  
chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/$SOLR /usr/local/share/solr-
config  
  
## martin county specific  
COPY /solr/ /opt/solr/example/solr/collection1/conf  
## end martin county specific  
EXPOSE 8983  
WORKDIR /opt/solr  
USER $SOLR_USER  
  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]  

