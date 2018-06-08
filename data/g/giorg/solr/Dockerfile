FROM java:openjdk-8-jre  
MAINTAINER Guillaume Giordana "guillaume.giordana@the-oz.com"  
ENV SOLR_VERSION 3.6.1  
ENV SOLR apache-solr-$SOLR_VERSION  
ENV SOLR_USER solr  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install lsof && \  
groupadd -r $SOLR_USER && \  
useradd -r -g $SOLR_USER $SOLR_USER && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/$SOLR  
  
EXPOSE 8983  
WORKDIR /opt/solr  
USER $SOLR_USER  
CMD cd /opt/$SOLR/theoz/ && java -Dsolr.solr.home=multicore -jar start.jar

