FROM ubuntu:14.04  
MAINTAINER Paul Velez "paul@relayrides.com"  
# Install java  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update -y && \  
apt-get install -y oracle-java7-installer \  
oracle-java7-set-default \  
tar \  
wget  
  
# Install Solr 4.x.  
ENV SOLR_VERSION 4.2.1  
RUN mkdir -p /opt && \  
wget -nv
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz
-O /opt/solr-$SOLR_VERSION.tgz && \  
tar -C /opt --extract --file /opt/solr-$SOLR_VERSION.tgz && \  
mv /opt/solr-$SOLR_VERSION/example /opt/solr && \  
rm -rf /opt/solr-$SOLR_VERSION.tgz /opt/solr-$SOLR_VERSION  
  
# Start solr  
WORKDIR /opt/solr  
VOLUME ["/data/solr"]  
EXPOSE 8983  
CMD [ "/usr/bin/java", "-Dsolr.solr.home=/data/solr", "-jar", "start.jar" ]  

