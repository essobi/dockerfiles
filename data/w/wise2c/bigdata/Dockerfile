FROM openjdk:8  
MAINTAINER mian <gopher.mian@outlook.com>  
  
WORKDIR /root  
  
# install openssh-server  
RUN apt-get update && apt-get install -y supervisor openssh-server && rm -rf
/var/lib/apt/lists/*  
  
# install hadoop 2.7.4  
RUN curl -O
http://www.namesdir.com/mirrors/apache/hadoop/common/hadoop-2.7.4/hadoop-2.7.4.tar.gz
&& \  
tar -xzvf hadoop-2.7.4.tar.gz && \  
mv hadoop-2.7.4 /usr/local/hadoop && \  
rm hadoop-2.7.4.tar.gz  
  
# set environment variable  
ENV HADOOP_HOME=/usr/local/hadoop  
ENV PATH=$PATH:/usr/local/hadoop/bin:/usr/local/hadoop/sbin  
  
# ssh without key  
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
sed -i "s/# StrictHostKeyChecking ask/StrictHostKeyChecking no/g"
/etc/ssh/ssh_config  
  
ADD config /usr/local/hadoop/etc/hadoop/  
  
ADD tool /tool/  
  
ADD supervisord /supervisord

