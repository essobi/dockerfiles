####  
#  
# Dockerfile for building a Apache Solr;  
#  
# with scope to ckan  
#  
####  
FROM eccenca/baseimage:v1.2.0  
MAINTAINER Henri Knochenhauer <henri.knochenhauer@eccenca.com>  
MAINTAINER René Pietzsch <rene.pietzsch@eccenca.com>  
  
  
#set env  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Java  
RUN apt-get -q -y update && \  
apt-get -q -y install default-jre-headless  
  
# Install Solr  
ENV \  
SOLR_HOME=/opt/solr/example/solr \  
SOLR_VERSION=4.10.4 \  
CKAN_VERSION=2.2.3  
RUN mkdir -p /opt/solr  
# In 17.06-ce this command unarchive tgz automatically to
/opt/solr-4.10.4.tgz/solr-4.10.4  
#ADD
https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz
/opt/solr-$SOLR_VERSION.tgz  
RUN wget
https://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz
-O /opt/solr-$SOLR_VERSION.tgz  
RUN tar zxf /opt/solr-$SOLR_VERSION.tgz -C /opt/solr --strip-components 1  
  
# Install CKAN Solr core  
RUN cp -R $SOLR_HOME/collection1/ $SOLR_HOME/ckan/  
RUN echo name=ckan > $SOLR_HOME/ckan/core.properties  
# There is no schema.xml in this repository  
#ADD schema.xml $SOLR_HOME/ckan/conf/schema.xml  
# Changed to wget to have more consistent image  
ADD
https://github.com/ckan/ckan/raw/ckan-$CKAN_VERSION/ckan/config/solr/schema.xml
$SOLR_HOME/ckan/conf/schema.xml  
RUN wget
https://github.com/ckan/ckan/raw/ckan-$CKAN_VERSION/ckan/config/solr/schema.xml
-O $SOLR_HOME/ckan/conf/schema.xml  
  
EXPOSE 8983  
WORKDIR /opt/solr/example  
CMD ["java", "-jar", "start.jar"]  

