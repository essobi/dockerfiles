FROM ubuntu:14.04  
MAINTAINER Leandro Gomez<lgomez@devartis.com>  
RUN apt-get update && apt-get -y install openjdk-7-jdk wget jetty8 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;  
  
RUN cd /opt && \  
wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz && \  
tar -xvf solr-4.7.2.tgz && cp -R solr-4.7.2/example /opt/solr  
  
RUN mv /opt/solr/solr/collection1 /opt/solr/solr/ckan && \  
echo "name=ckan" > /opt/solr/solr/ckan/core.properties  
ADD
https://raw.githubusercontent.com/ckan/ckan/ckan-2.7.4/ckan/config/solr/schema.xml
\  
/opt/solr/solr/ckan/conf/schema.xml  
COPY jetty.defaults /etc/defaults/jetty  
COPY jetty-logging.xml /opt/solr/etc/  
RUN useradd -d /opt/solr -s /sbin/false solr && chown solr:solr -R /opt/solr  
USER solr  
  
WORKDIR /opt/solr/  
  
EXPOSE 8983  
CMD ["java", "-jar", "start.jar"]

