FROM makuk66/docker-oracle-java7  
MAINTAINER Istvan Palocz "istvan@palocz.hu"  
ENV SOLR_VERSION 3.5.0  
ENV SOLR solr-$SOLR_VERSION  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install lsof curl procps && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://ftp.nchu.edu.tw/Unix/Web/apache/lucene/solr/$SOLR_VERSION/apache-
solr-$SOLR_VERSION.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr  
  
COPY solr-conf/3.x/* /opt/apache-solr-3.5.0/example/solr/conf/  
COPY solr.xml /opt/apache-solr-3.5.0/example/solr/solr.xml  
  
VOLUME /opt/apache-solr-3.5.0/example/solr/data  
VOLUME /opt/apache-solr-3.5.0/example/logs  
  
EXPOSE 8983  
COPY start.sh /start.sh  
CMD ["bash", "/start.sh"]  

