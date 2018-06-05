FROM ubuntu:12.04  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
RUN apt-get install -y make gcc wget openjdk-6-jre  
RUN wget http://archive.apache.org/dist/lucene/solr/3.6.2/apache-
solr-3.6.2.tgz -O /tmp/pkg.tar.gz  
RUN (cd /tmp && tar zxf pkg.tar.gz && mv apache-solr-* /opt/solr)  
RUN rm -rf /tmp/*  
ADD run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
EXPOSE 8983  
CMD ["/usr/local/bin/run"]  

