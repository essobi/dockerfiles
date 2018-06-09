FROM ubuntu:14.04  
MAINTAINER Paolo Mainardi <paolo@twinbit.it>  
ENV DEBIAN_FRONTEND noninteractive  
  
# install java and wget  
RUN apt-get update && \  
apt-get install -y \  
curl \  
openjdk-7-jre-headless \  
unzip \  
wget \  
lsof \  
curl \  
procps  
  
ENV SOLR_VERSION 4.10.2  
ENV SOLR solr-$SOLR_VERSION  
  
# download and install solr  
WORKDIR /tmp  
RUN mkdir -p /opt && \  
wget --progress=bar:force --output-document=/opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr  
  
# Release from search_api_solr  
# https://www.drupal.org/node/982682/release  
ENV SEARCH_API_SOLR_VERSION=7.x-1.10  
# Dowload and copy configuration  
RUN export SOLR_MAJOR_VERSION=`echo $SOLR_VERSION | cut -f1 -d.` && \  
env && \  
wget --progress=bar:force --output-document=/tmp/search_api_solr.zip \  
https://ftp.drupal.org/files/projects/search_api_solr-$SEARCH_API_SOLR_VERSION.zip
&& \  
unzip /tmp/search_api_solr.zip -d /tmp/search_api_solr && \  
cp -r /tmp/search_api_solr/search_api_solr/solr-conf/$SOLR_MAJOR_VERSION.x/*
/opt/solr/example/solr/collection1/conf/ && \  
rm -rf /tmp/search_api_solr  
  
EXPOSE 8983  
WORKDIR /opt/solr/example  
ENTRYPOINT ["java"]  
CMD ["-Xmx512m", "-DSTOP.PORT=8079", "-DSTOP.KEY=stopkey", "-jar",
"start.jar"]  

