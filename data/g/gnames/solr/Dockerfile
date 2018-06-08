FROM gnames/resolver:latest  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2016-02-20  
ENV SOLR_VERSION 3.5.0  
ENV SOLR apache-solr-$SOLR_VERSION  
ENV SOLR_DOWNLOAD
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz  
  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install git lsof wget vim-nox curl procps \  
openjdk-7-jre-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -nv --output-document=/opt/$SOLR.tgz $SOLR_DOWNLOAD && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
mv /opt/$SOLR /opt/solr && \  
rm -rf /opt/solr/example/solr && \  
mv /app/solr/multicore /opt/solr/example/solr  
  
EXPOSE 8983  
WORKDIR /opt/solr/example  
  
CMD [ "/bin/bash", "-c", "/usr/bin/java -Xmx30g
-Dsolr.solr.home=/opt/solr/example/solr -jar start.jar"]  
  

