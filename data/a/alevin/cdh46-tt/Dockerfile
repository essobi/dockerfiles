FROM centos:centos6  
  
MAINTAINER Alex Levin  
  
RUN yum -y install lzo lzo-devel sudo wget  
  
RUN wget -q -O /tmp/jdk-7u67-linux-x64.rpm --no-check-certificate --no-cookies
--header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.rpm  
RUN yum -y localinstall /tmp/jdk-7u67-linux-x64.rpm  
  
RUN rpm --import http://archive.cloudera.com/cdh4/redhat/6/x86_64/cdh/RPM-GPG-
KEY-cloudera  
  
COPY inst/cdh4.repo /etc/yum.repos.d/cdh4.repo  
COPY inst/cloudera-gplextras4.repo /etc/yum.repos.d/cloudera-gplextras4.repo  
  
RUN yum -y install hadoop  
RUN yum -y install hadoop-hdfs-datanode hadoop-0.20-mapreduce-tasktracker
hadoop-lzo-cdh4  
  
RUN rm /etc/hadoop/conf  
RUN mkdir /etc/hadoop/conf  
RUN mkdir /data  
RUN chmod 777 /data  
  
COPY inst/run.sh /run.sh  
  
ENTRYPOINT ["/bin/bash", "/run.sh" ]  
EXPOSE 50060  

