FROM centos:7.2.1511  
MAINTAINER Craig Willis (willis8@illinois.edu)  
  
RUN yum install -y wget unzip perl git java-1.8.0-openjdk-devel
postgresql.x86_64  
  
# Install Solr 4.6.0  
RUN cd /tmp && wget
https://archive.apache.org/dist/lucene/solr/4.6.0/solr-4.6.0.tgz && \  
tar xvzf solr-4.6.0.tgz && \  
mv solr-4.6.0 /usr/local/ && \  
cd /usr/local/solr-4.6.0/example/solr/collection1/conf/ && \  
mv schema.xml schema.xml.backup && \  
wget -q --no-check-certificate
https://github.com/IQSS/dataverse/raw/master/conf/solr/4.6.0/schema.xml && \  
rm /tmp/solr-4.6.0.tgz  
  
RUN ln -s /usr/local/solr-4.6.0/example/logs /var/log/solr  
  
VOLUME /usr/local/solr-4.6.0/example/solr/collection1/data  
  
EXPOSE 8983  
COPY Dockerfile /Dockerfile  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["solr"]  

