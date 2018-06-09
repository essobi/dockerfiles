FROM phusion/baseimage:0.9.16  
MAINTAINER Gregor Weckbecker <gregor@codevise.de>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y openjdk-7-jre-headless && apt-get
clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV SOLR_VERSION 4.9.1  
ENV SOLR solr-$SOLR_VERSION  
ENV DATA_DIR /data/solr/solr/production  
  
RUN curl --retry 3
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz | tar -C
/opt --extract --gzip  
RUN mv /opt/$SOLR /opt/solr  
  
RUN mkdir -p /etc/service/solr  
ADD deploy/run/solr.sh /etc/service/solr/run  
  
ADD newrelic.tgz /opt  
  
RUN mkdir -p /data/solr  
RUN useradd --home-dir /data/solr --comment "Solr Server" solr  
RUN chown -R solr:solr /data/solr  
  
VOLUME $DATA_DIR  
  
ADD solr /data/solr  
RUN chown -R solr:solr /data/solr  
  
EXPOSE 8983  
WORKDIR /data/solr  

