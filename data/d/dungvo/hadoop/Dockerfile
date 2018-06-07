FROM dungvo/java  
MAINTAINER Dung Vo [cdung.vo@gmail.com]  
  
USER root  
  
ENV HADOOP_VERSION 2.7.3  
ENV URL
http://supergsego.com/apache/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz  
#ENV URL http://172.30.113.110/dungcv/hadoop-${HADOOP_VERSION}.tar.gz  
ENV INSTALLATION_PATH /usr/local  
  
  
# Install OpenSSH  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
supervisor \  
wget \  
curl  
  
RUN mkdir /var/run/sshd \  
# Set password for root \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
# SSH login fix. Otherwise user is kicked off after login \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
# passwordless ssh \  
&& ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa \  
&& cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys  
  
ADD ssh_config /root/.ssh/config  
  
# ENV NOT-VISIBLE  
ENV VISIBLE now  
  
EXPOSE 22  
# Install Hadoop  
RUN wget ${URL} -O /tmp/hadoop-${HADOOP_VERSION}.tar.gz \  
&& cd /tmp \  
&& tar xzf hadoop-${HADOOP_VERSION}.tar.gz \  
&& rm hadoop-${HADOOP_VERSION}.tar.gz \  
&& mv hadoop-${HADOOP_VERSION} ${INSTALLATION_PATH}/hadoop  
  
# Enviroments Hadoop  
ENV HADOOP_HOME ${INSTALLATION_PATH}/hadoop  
ENV HADOOP_PREFIX ${INSTALLATION_PATH}/hadoop  
ENV HADOOP_COMMON_HOME ${INSTALLATION_PATH}/hadoop  
ENV HADOOP_HDFS_HOME ${INSTALLATION_PATH}/hadoop  
ENV HADOOP_MAPRED_HOME ${INSTALLATION_PATH}/hadoop  
ENV HADOOP_YARN_HOME ${INSTALLATION_PATH}/hadoop  
ENV HADOOP_CONF_DIR ${INSTALLATION_PATH}/hadoop/etc/hadoop  
ENV YARN_CONF_DIR ${INSTALLATION_PATH}/hadoop/etc/hadoop  
RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/opt/jdk\nexport
HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
# Pseudo distributed  
ADD conf/core-site.xml ${HADOOP_CONF_DIR}/core-site.xml  
ADD conf/hdfs-site.xml ${HADOOP_CONF_DIR}/hdfs-site.xml  
ADD conf/mapred-site.xml ${HADOOP_CONF_DIR}/mapred-site.xml  
ADD conf/yarn-site.xml ${HADOOP_CONF_DIR}/yarn-site.xml  
ADD conf/capacity-scheduler.xml ${HADOOP_CONF_DIR}/capacity-scheduler.xml  
# HDFS ports  
EXPOSE 9000 50070  
# YARN ports  
EXPOSE 8040 8042 8088 8030 8031 8032 8033  
# Start ssh  
ADD startup.sh ${INSTALLATION_PATH}/bin/startup.sh  
RUN chmod +x ${INSTALLATION_PATH}/bin/startup.sh  
  
WORKDIR ${HADOOP_HOME}  
  
CMD ["startup.sh"]  

