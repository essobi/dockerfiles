FROM openjdk:8  
MAINTAINER mian <gopher.mian@outlook.com>  
  
WORKDIR /root  
  
# install openssh-server  
RUN apt-get update && apt-get install -y supervisor openssh-server && rm -rf
/var/lib/apt/lists/*  
  
# install hbase 1.2.4  
RUN curl -O
https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/1.2.4/hbase-1.2.4-bin.tar.gz
&& \  
tar -xzvf hbase-1.2.4-bin.tar.gz && \  
mv hbase-1.2.4 /usr/local/hbase && \  
rm hbase-1.2.4-bin.tar.gz  
  
# set environment variable  
ENV HBASE_HOME=/usr/local/hbase  
ENV PATH=$PATH:/usr/local/hbase/bin  
  
# ssh without key  
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
sed -i "s/# StrictHostKeyChecking ask/StrictHostKeyChecking no/g"
/etc/ssh/ssh_config  

