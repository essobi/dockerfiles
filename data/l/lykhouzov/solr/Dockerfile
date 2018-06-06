FROM centos:7  
MAINTAINER Aleksandr Lykhouzov <lykhouzov@gmail.com>  
  
# Install  
RUN yum -y update && yum install -y wget java \  
&& yum clean all \  
&& cd /opt/ \  
&& wget https://archive.apache.org/dist/lucene/solr/5.3.1/solr-5.3.1.tgz \  
&& tar zxvf solr-5.3.1.tgz \  
&& mv solr-5.3.1 solr_01 \  
&& rm -f solr-5.3.1.tgz  
  
COPY ./conf/* /opt/solr_01/example/solr/conf/  
  
EXPOSE 8080 8983  
WORKDIR /opt/solr_01/example  
CMD
["java","-Djetty.home=/opt/solr_01/example","-jar","/opt/solr_01/example/start.jar"]  

