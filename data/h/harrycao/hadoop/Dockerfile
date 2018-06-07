FROM centos:6.9  
MAINTAINER caohui <iamcaohui@gmail.com>  
  
WORKDIR /root  
  
RUN yum update -y && \  
yum install -y initscripts openssh-server openssh-clients && \  
yum clean all  
  
RUN curl -LO "http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm"
-H 'Cookie: oraclelicense=accept-securebackup-cookie' && \  
rpm -ivh ./jdk-8u131-linux-x64.rpm && \  
rm -f ./jdk-8u131-linux-x64.rpm  
  
RUN mkdir -p /usr/local/hadoop/ && \  
curl -LO "https://github.com/harrycao/hadoop-
docker/releases/download/hadoop-v2.8.0/hadoop-2.8.0.tar.gz" && \  
tar -xzf ./hadoop-2.8.0.tar.gz -C /usr/local/hadoop/ && \  
rm -f ./hadoop-2.8.0.tar.gz  
  
COPY ssh-config /root/.ssh/config  
  
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
chmod 644 ~/.ssh/authorized_keys  
  
ENV JAVA_HOME=/usr/java/jdk1.8.0_131  
ENV HADOOP_HOME=/usr/local/hadoop/hadoop-2.8.0  
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin  
  
COPY hadoop-conf/* $HADOOP_HOME/etc/hadoop/  
  
RUN mkdir -p ~/hdfs/name ~/hdfs/data && \  
chown root:root $HADOOP_HOME/etc/hadoop/* && \  
hdfs namenode -format  
  
CMD service sshd start; bash

