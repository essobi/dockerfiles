FROM java:8  
  
MAINTAINER Jean Traullé jean@oblady.fr  
  
ENV SOLR_VERSION 4.8.1  
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
mv /opt/$SOLR /opt/solr && \  
wget -nv https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.0.8.tar.gz && \  
tar -xzf /mysql-connector-java-5.0.8.tar.gz && \  
mv /mysql-connector-java-5.0.8/mysql-connector-java-5.0.8-bin.jar
/opt/solr/dist/ && \  
rm -rf /mysql-connector-java-5.0.8.tgz /mysql-connector-java-5.0.8  
  
EXPOSE 8983  
WORKDIR /opt/solr  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]  

