FROM centos  
  
# Based on centos:7.2.1511 Public Image  
MAINTAINER "larry king" <jiangguoqing@stars.org.cn>`  
  
# set cloudera repository  
RUN echo -e "# Packages for Cloudera's Distribution for Hadoop, Version 5, on
RedHat or CentOS 7 x86_64\n[cloudera-cdh5]\nname=Cloudera's Distribution for
Hadoop, Version
5\nbaseurl=https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/5/\ngpgkey
=https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/RPM-GPG-KEY-
cloudera\ngpgcheck = 1" > /etc/yum.repos.d/cloudera.repo  
  
# install jdk1.8  
#RUN yum install -y java-1.8.0-openjdk-1.8.0.111  
COPY jdk1.8 /jdk1.8  
# File was splited using: split -b 20m  
WORKDIR /jdk1.8  
  
RUN echo "Generating jdk-8u101-linux-x64.tar.tgz file" && \  
cat x* > jdk-8u101-linux-x64.tar.tgz && \  
rm -rf x* && \  
tar -xzf jdk-8u101-linux-x64.tar.tgz && \  
rm -rf jdk-8u101-linux-x64.tar.tgz  
  
# install vim & net-tools  
RUN yum install -y vim && \  
yum install -y net-tools  
  
# install latest version of impala  
RUN yum install -y impala impala-server impala-state-store impala-catalog
impala-shell  
  
# set JAVA_HOME  
RUN echo "export JAVA_HOME=/jdk1.8/jdk1.8.0_101" >> /etc/default/bigtop-utils  
  
# add hadoop hive configure  
COPY config/core-site.xml /etc/impala/conf/core-site.xml  
COPY config/hive-site.xml /etc/impala/conf/hive-site.xml  
COPY config/hdfs-site.xml /etc/impala/conf/hdfs-site.xml  
  
# add mysql-connector-jar  
COPY mysql-connector-jar/mysql-connector-java.jar /usr/share/java/mysql-
connector-java.jar  
  
# move impala configure base info  
COPY config/impala /etc/default/config.txt  
  
# depoly bash script of impala configure info  
RUN mkdir /impala  
COPY depoly_impala_config.sh /impala/depoly_impala_config.sh  
RUN chmod a+x /impala/depoly_impala_config.sh  
  
# CMD  
CMD [ "/bin/bash" ]  

