  
FROM centos:6.6  
MAINTAINER Pradeep Aradhya "pradeep4aradhya@gmail.com"  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y update && yum clean all  
  
RUN yum install -y java-1.7.0-openjdk.x86_64 java-1.7.0-openjdk-devel.x86_64
wget tar  
  
ENV SOLR_VERSION 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
RUN yum -y install lsof curl procps && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://www.mirrorservice.org/sites/ftp.apache.org/lucene/solr/$SOLR_VERSION/$SOLR.tgz
&& \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr  
  
EXPOSE 8983  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr"]  

