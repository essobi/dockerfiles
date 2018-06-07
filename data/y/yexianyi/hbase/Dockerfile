# This docker file is for Hbase1.2.0 standalone.  
FROM ubuntu:16.04  
  
ARG JDK_VERSION=jdk-8u101  
ARG JDK_PACKAGE=$JDK_VERSION-linux-x64.tar.gz  
ARG JDK_INSTALL_PATH=/usr/lib/java  
  
ARG HADOOP_VERSION=2.7.3  
ARG HADOOP_PACKAGE=hadoop-$HADOOP_VERSION.tar.gz  
ARG HADOOP_INSTALL_PATH=/home  
  
ARG HBASE_VERSION=1.2.3  
ARG HBASE_PACKAGE=hbase-$HBASE_VERSION-bin.tar.gz  
ARG HBASE_INSTALL_PATH=/home  
  
ENV JAVA_HOME=$JDK_INSTALL_PATH/jdk1.8.0_101 \  
HBASE_HOME=$HBASE_INSTALL_PATH/hbase-$HBASE_VERSION \  
HADOOP_HOME=$HADOOP_INSTALL_PATH/hadoop-$HADOOP_VERSION  
ENV
PATH=$JAVA_HOME/bin:$HBASE_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH  
  
  
MAINTAINER Xianyi Ye <https://cn.linkedin.com/in/yexianyi>  
RUN sed -i 's/archive.ubuntu.com/hk.archive.ubuntu.com/g'
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y wget ssh sshpass rsync\  
&& apt-get clean \  
&& apt-get autoremove \  
  
# Config SSH  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config \  
&& service ssh start \  
&& echo "root:root" | chpasswd \  
&& mkdir -p ~/.ssh \  
&& cd ~/.ssh \  
&& ssh-keygen -t rsa -N "" -f root.key \  
&& cat root.key.pub >> authorized_keys \  
&& chmod 600 authorized_keys \  
&& rm root.key.pub \  
&& sshpass -p "root" scp -o "StrictHostKeyChecking no" localhost:.ssh/root.key
myserver.rsa \  
&& chmod 600 myserver.rsa \  
&& echo "HOST localhost" >> config \  
&& echo "Hostname localhost" >> config \  
&& echo "IdentityFile ~/.ssh/myserver.rsa" >> config \  
  
# Install Oracle JDK  
&& mkdir /usr/lib/java \  
&& cd /usr/lib/java \  
&& wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u101-b13/$JDK_PACKAGE \  
&& tar -xzvf $JDK_PACKAGE \  
&& rm ./$JDK_PACKAGE \  
  
#Install Hadoop  
&& cd /home \  
&& wget http://www-eu.apache.org/dist/hadoop/common/stable/$HADOOP_PACKAGE \  
&& tar xzvf $HADOOP_PACKAGE \  
&& rm -f $HADOOP_PACKAGE \  
&& rm -rf $HBASE_HOME/share/doc/ \  
  
#Config Hadoop  
&& cd $HADOOP_HOME/etc/hadoop \  
&& rm -f core-site.xml hdfs-site.xml \  
&& wget https://raw.githubusercontent.com/yexianyi/hbase/pseudo-
clustering-1.2.3/etc/hadoop/core-site.xml \  
&& wget https://raw.githubusercontent.com/yexianyi/hbase/pseudo-
clustering-1.2.3/etc/hadoop/hdfs-site.xml \  
&& sed -i 's#${JAVA_HOME}#'$JAVA_HOME'#g' ./hadoop-env.sh \  
&& echo 'export JAVA_HOME='$JAVA_HOME >> ~/.bashrc \  
&& echo 'export HBASE_HOME='$HBASE_HOME >> ~/.bashrc \  
&& echo 'export HADOOP_HOME='$HADOOP_HOME >> ~/.bashrc \  
&& echo 'export PATH='$PATH >> ~/.bashrc \  
  
# Install HBase  
&& cd /home \  
&& wget http://apache.claz.org/hbase/$HBASE_VERSION/$HBASE_PACKAGE \  
&& tar xzvf $HBASE_PACKAGE \  
&& rm -f $HBASE_PACKAGE \  
&& rm -rf $HBASE_HOME/docs/ \  
  
# Config HBase Standalone  
&& cd $HBASE_HOME/conf \  
&& rm -f hbase-env.sh hbase-site.xml \  
&& wget
https://raw.githubusercontent.com/yexianyi/hbase/standalone-1.2.3/conf/hbase-
env.sh \  
&& wget
https://raw.githubusercontent.com/yexianyi/hbase/standalone-1.2.3/conf/hbase-
site.xml  
  
# HDFS Web Interface 50070  
# Master Web Interface 16010  
# RegionServer Web Interface 16030  
# Zookeeper 2181  
EXPOSE 50070 16010 16030 8088 2181  
CMD service ssh start \  
&& hdfs namenode -format \  
&& start-dfs.sh \  
&& start-hbase.sh  

