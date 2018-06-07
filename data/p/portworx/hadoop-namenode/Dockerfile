FROM centos:7  
MAINTAINER Portworx  
  
USER root  
  
RUN yum clean all; \  
rpm --rebuilddb;  
RUN yum install -y curl tar sudo which openssh-server openssh-clients rsync  
  
# TEMP stuff  
#RUN yum install -y net-tools telnet  
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
oraclelicense=accept-securebackup-cookie' && rpm -i jdk-7u71-linux-x64.rpm &&
rm jdk-7u71-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  
  
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
  
RUN mkdir $HADOOP_PREFIX/input $HADOOP_PREFIX/logs && \  
cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input && \  
rm $HADOOP_PREFIX/etc/hadoop/core-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-
site.xml && \  
chmod +x $HADOOP_PREFIX/etc/hadoop/*.sh  
  
# Copy modified XML and other config files to /etc/hadoop  
COPY hdfs-site.xml.template $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml.template  
COPY mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
COPY core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
COPY slaves $HADOOP_PREFIX/etc/hadoop/slaves  
  
#MORE TEMP STUFF  
#COPY log4j.properties.temp $HADOOP_PREFIX/etc/hadoop/log4j.properties  
# create data  
#RUN mkdir -p /hdfs/volume1  
VOLUME /hdfs/volume1  
  
# Expose Ports  
EXPOSE 22  
EXPOSE 9000  
EXPOSE 50070  
EXPOSE 50090  
COPY namenode-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

