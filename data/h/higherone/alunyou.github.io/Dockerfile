FROM higherone/alunyou.github.io:ubuntu-jdk8  
MAINTAINER Alun  
  
USER root  
  
ENV TERM xterm  
  
#RUN apt-get update  
RUN apt-get install -y vim curl ssh openssh-server  
  
#ssh passphraseless  
RUN ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa;\  
cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys;\  
chmod 0600 ~/.ssh/authorized_keys;\  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config;\  
echo "ListenAddress 0.0.0.0" >> /etc/ssh/sshd_config  
  
#sshd needs this  
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
#port  
EXPOSE 22  
#install native support  
RUN mkdir -p /tmp/native;\  
curl -Ls http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.7.0.tar | tar -x -C /tmp/native;  
  
#link  
RUN cd /usr/local && ln -s /mnt_host/docker/hadoop-2.7.2 hadoop  
RUN cd /usr/local && ln -s /mnt_host/docker/apache-hive-2.0.0-bin hive  
  
ENV HIVE_HOME /usr/local/hive  
ENV HADOOP_HOME /usr/local/hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_LOG_DIR /usr/local/hadoop/logs  
ENV HADOOP_MAPRED_LOG_DIR /usr/local/hadoop/logs  
  
  

