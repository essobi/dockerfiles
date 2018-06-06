FROM ubuntu:16.04  
LABEL maintainer="Kamil Szewczyk <szewinho@gmail.com>"  
  
RUN apt-get update && apt-get install -y --no-install-recommends software-
properties-common && \  
add-apt-repository ppa:webupd8team/java  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && apt-get install -y vim iputils-ping rsync openssh-server
&& \  
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
chmod 600 ~/.ssh/authorized_keys  
  
RUN cd /opt && wget -q
https://archive.apache.org/dist/hadoop/core/hadoop-2.7.1/hadoop-2.7.1.tar.gz
&& \  
tar -xzf hadoop-2.7.1.tar.gz && rm -f hadoop-2.7.1.tar.gz && \  
ln -s hadoop-2.7.1 hadoop  
  
ENV HADOOP_HOME="/opt/hadoop"  
ENV PATH=$PATH:$HADOOP_HOME/bin  
ENV PATH=$PATH:$HADOOP_HOME/sbin  
ENV HADOOP_MAPRED_HOME=${HADOOP_HOME}  
ENV HADOOP_COMMON_HOME=${HADOOP_HOME}  
ENV HADOOP_HDFS_HOME=${HADOOP_HOME}  
ENV YARN_HOME=${HADOOP_HOME}  
ENV HADOOP_PREFIX=${HADOOP_HOME}  
  
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop  
ENV YARN_CONF_DIR=${HADOOP_HOME}/etc/hadoop  
  
ENV HDFS_NAMENODE_USER=root  
ENV HDFS_DATANODE_USER=root  
ENV HDFS_SECONDARYNAMENODE_USER=root  
  
ENV HDFS_REPLICATION=1  
RUN sed -i "s,^export JAVA_HOME=\${JAVA_HOME},export
JAVA_HOME=/usr/lib/jvm/java-8-oracle,g" /opt/hadoop/etc/hadoop/hadoop-env.sh  
  
ADD core-site.xml.template /opt/templates/  
ADD hdfs-site.xml.template /opt/templates/  
  
ADD bootstrap.sh /opt/bootstrap.sh  
RUN chmod 700 /opt/bootstrap.sh  
  
CMD ["/opt/bootstrap.sh", "-d"]  

