FROM centos:7  
MAINTAINER Portworx  
  
USER root  
  
RUN yum install -y curl tar sudo which openssh-server openssh-clients rsync  
  
# SSH and user equivalence  
RUN rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t ed25519 -f /etc/ssh/ssh_host_ed25519_key && \  
sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config  
  
RUN mkdir -p /root/.ssh  
COPY id_rsa /root/.ssh/id_rsa  
COPY id_rsa.pub /root/.ssh/id_rsa.pub  
COPY id_rsa.pub /root/.ssh/authorized_keys  
COPY ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config && chown root:root /root/.ssh/config  
  
# java  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie' && \  
rpm -i jdk-7u71-linux-x64.rpm && \  
rm jdk-7u71-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_PREFIX/bin  
  
RUN curl -s
http://www.us.apache.org/dist/hadoop/common/hadoop-2.7.1/hadoop-2.7.1.tar.gz |
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.7.1 hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
  
ENV HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop  
ENV JAVA_HOME=/usr/java/default  
  
# A few fixes  
RUN mkdir $HADOOP_PREFIX/input && cp $HADOOP_PREFIX/etc/hadoop/*.xml
$HADOOP_PREFIX/input  
  
# remove these - we need to set the hostname of the instance in this file  
RUN rm -f $HADOOP_PREFIX/etc/hadoop/yarn-site.xml
$HADOOP_PREFIX/etc/hadoop/core-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-
site.xml  
  
# Copy modified XML and other config files to /etc/hadoop  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
ADD yarn-site.xml.template $HADOOP_PREFIX/etc/hadoop/yarn-site.xml.template  
ADD yarn-site.xml.template $HADOOP_PREFIX/etc/hadoop/yarn-site.xml.template  
ADD mapred-site.xml.template $HADOOP_PREFIX/etc/hadoop/mapred-
site.xml.template  
ADD slaves $HADOOP_PREFIX/etc/hadoop/slaves  
  
# Fix perms  
RUN rm -rf $HADOOP_PREFIX/etc/hadoop/*.cmd && chmod +x
$HADOOP_PREFIX/etc/hadoop/*.sh  
  
# create data  
RUN mkdir -p /hdfs/volume1  
  
VOLUME /hdfs/volume1  
  
# Expose Ports  
EXPOSE 22  
EXPOSE 8030  
EXPOSE 8031  
EXPOSE 8032  
EXPOSE 8033  
EXPOSE 8088  
EXPOSE 10020  
EXPOSE 19888  
COPY yarn-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

