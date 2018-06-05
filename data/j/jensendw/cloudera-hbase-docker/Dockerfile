FROM centos:7.2.1511  
MAINTAINER Daniel Jensen <jensendw@gmail.com>  
  
ARG CDH_VERSION=5.5.0  
ARG DOCKERIZE_VERSION=v0.2.0  
ARG HBASE_VERSION=1.0.0+cdh5.5.0+269  
# Install required packages  
RUN yum install -y java wget  
  
# Fetch and install the CDH repo  
RUN wget -O /tmp/cdh.rpm https://archive.cloudera.com/cdh5/one-click-
install/redhat/7/x86_64/cloudera-
cdh-5-0.x86_64.rpm?_ga=1.149065204.314357562.1443746297  
RUN yum -y --nogpgcheck localinstall /tmp/cdh.rpm  
  
# Replace CDH5 repo version with specific version instead of latest  
RUN sed -i s@/5/@/$CDH_VERSION/@g /etc/yum.repos.d/cloudera-cdh5.repo  
  
# Clean up cache so we can pick up the new CDH repo  
RUN yum clean all  
  
# Install Hbase client which will also install a bunch of dependencies  
RUN yum -y install hbase-$HBASE_VERSION  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
COPY files/etc/hbase/conf/* /etc/hbase/conf/  
  
CMD dockerize -template /etc/hbase/conf/hbase-site.tmpl:/etc/hbase/conf/hbase-
site.xml -template /etc/hbase/conf/hdfs-site.tmpl:/etc/hbase/conf/hdfs-
site.xml  

