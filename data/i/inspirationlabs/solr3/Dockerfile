FROM phusion/baseimage  
  
RUN apt-get update  
RUN apt-get install -y wget default-jre-headless  
  
ENV SOLR_VERSION 3.6.2  
RUN wget http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/apache-
solr-$SOLR_VERSION.tgz -O /tmp/solr-$SOLR_VERSION.tgz  
RUN cd /usr/share && tar zxf /tmp/solr-$SOLR_VERSION.tgz  
RUN mv /usr/share/apache-solr-$SOLR_VERSION /usr/share/solr  
RUN cp -a /usr/share/solr/example /usr/share/solr/main  
RUN mkdir -p /var/solr  
  
EXPOSE 8983  
VOLUME ["/var/solr"]  
  
CMD cd /usr/share/solr/main && java -Dsolr.solr.home=/var/solr -jar start.jar  

