FROM ferronrsmith/serf  
MAINTAINER Ferron Hanse  
  
# Versions  
ENV CDH_MAJOR 5  
ENV CDH_VERSION 5.3.1  
# Installing Oracle JDK  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update && apt-get upgrade -y  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Cloudera CDH5 APT key and DPKG repositories  
RUN apt-get -y install curl ;\  
curl -s http://archive.cloudera.com/cdh5/ubuntu/precise/amd64/cdh/archive.key
| apt-key add - ;\  
echo "deb [arch=amd64]
http://archive.cloudera.com/cdh$CDH_MAJOR/ubuntu/precise/amd64/cdh precise-
cdh$CDH_VERSION contrib\n" > /etc/apt/sources.list.d/cloudera.list ;\  
echo "deb-src
http://archive.cloudera.com/cdh$CDH_MAJOR/ubuntu/precise/amd64/cdh precise-
cdh$CDH_VERSION contrib" >> /etc/apt/sources.list.d/cloudera.list ;\  
apt-get update  
  
# Installing FUSE  
RUN apt-get install -y hadoop-hdfs-fuse && mkdir -p /hdfs/dcc  
  
# Install command-line utils  
RUN apt-get install -y \  
vim.tiny \  
git \  
curl \  
tree \  
inetutils-ping \  
daemontools \  
dnsutils \  
sendemail  
  
RUN mkdir -p /etc/service/serf  
  
ADD config/service /etc/service  
  
RUN chmod +x /etc/service/serf/run  
  
ADD config/prep-hadoop.sh /opt/fuse/prep-hadoop.sh  
RUN chmod 755 opt/fuse/prep-hadoop.sh  
  
ENTRYPOINT ["/bin/bash", "/opt/fuse/prep-hadoop.sh"]

