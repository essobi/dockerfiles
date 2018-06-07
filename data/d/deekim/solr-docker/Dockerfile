# Solr 4.4.0 from CDH5.0.0 package distribution  
  
FROM ubuntu:12.04  
  
MAINTAINER Dan Kim "https://github.com/deekim"  
  
#########################  
# environment variables #  
#########################  
  
# cloudera  
ENV CDH5_VERSION 5.0.0  
  
# solr  
ENV SOLR_VERSION 4.4.0  
ENV SOLR solr-$SOLR_VERSION  
  
#########  
# setup #  
#########  
  
# update & update  
RUN apt-get update && apt-get -y upgrade  
  
# solr  
RUN mkdir -p /opt  
ADD http://archive.cloudera.com/cdh5/cdh/5/solr-$SOLR_VERSION-
cdh$CDH5_VERSION.tar.gz /opt/$SOLR.tar.gz  
RUN tar -xvzf /opt/$SOLR.tar.gz  
RUN ln -s /opt/$SOLR /opt/solr  
  
  
###########  
# startup #  
###########  
  
# CMD  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

