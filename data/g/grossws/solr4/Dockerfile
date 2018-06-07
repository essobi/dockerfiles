FROM grossws/tomcat8  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
ENV XTYPE=solr  
WORKDIR /opt  
  
ARG SOLR_VERSION=4.10.4  
ARG
SOLR_TGZ_URL=https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz  
  
RUN gpg --recv-keys $(curl
https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/KEYS | gpg --with-
fingerprint --with-colons | grep fpr | cut -d: -f10) \  
&& sed -i 's/8080/8983/' /opt/tomcat/conf/server.xml \  
&& mkdir -p /opt/solr/{data,conf,lib} \  
&& curl -sSL $SOLR_TGZ_URL -o solr.tar.gz \  
&& curl -sSL $SOLR_TGZ_URL.asc -o solr.tar.gz.asc \  
&& gpg --verify solr.tar.gz.asc solr.tar.gz \  
&& tar xvf solr.tar.gz -C /opt/tomcat/lib --strip-components=4
solr-$SOLR_VERSION/example/lib/ext/\\*.jar \  
&& tar xvf solr.tar.gz -C /opt/solr --strip-components=2
solr-$SOLR_VERSION/dist/solr-$SOLR_VERSION.war \  
&& tar xvf solr.tar.gz -C /opt/solr --strip-components=1
solr-$SOLR_VERSION/LICENSE.txt solr-$SOLR_VERSION/NOTICE.txt \  
&& mv solr/solr-$SOLR_VERSION.war solr/solr.war \  
&& mv solr/LICENSE.txt solr/LICENSE \  
&& mv solr/NOTICE.txt solr/NOTICE \  
&& echo "name = core0" > /opt/solr/core.properties \  
&& rm solr.tar.gz*  
  
ADD log4j.properties /opt/tomcat/lib/  
ADD catalina-solr.xml /opt/tomcat/conf/Catalina/localhost/solr.xml  
ADD solr.xml /opt/solr/  
  
VOLUME ["/opt/solr/data"]  
EXPOSE 8983  

