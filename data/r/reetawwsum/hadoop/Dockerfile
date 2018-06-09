FROM reetawwsum/machine-learning  
  
MAINTAINER Reet Awwsum <reetawwsum@yahoo.com>  
  
RUN yum install -y curl \  
openssh-clients \  
openssh-server \  
rsync \  
sudo \  
tar \  
which  
  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.rpm && \  
rpm -i jdk-8u111-linux-x64.rpm && \  
rm jdk-8u111-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
  
RUN rm /usr/bin/java && \  
ln -s $JAVA_HOME/bin/java /usr/bin/java  
  
RUN curl
http://www.eu.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz |
tar -xz -C /usr/local  
RUN ln -s /usr/local/hadoop-2.7.3 /usr/local/hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR /usr/local/hadoop/etc/hadoop  
  
ENV PATH $PATH:$HADOOP_PREFIX/bin  
  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN mkdir $HADOOP_PREFIX/input  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
ADD core-site.xml.template $HADOOP_PREFIX/etc/hadoop/core-site.xml.template  
RUN sed s/HOSTNAME/localhost/ /usr/local/hadoop/etc/hadoop/core-
site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
RUN /usr/sbin/sshd && \  
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
$HADOOP_PREFIX/sbin/start-dfs.sh && \  
$HADOOP_PREFIX/bin/hdfs dfs -mkdir -p /user/root  
  
RUN /usr/sbin/sshd && \  
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
$HADOOP_PREFIX/sbin/start-dfs.sh && \  
$HADOOP_PREFIX/bin/hdfs dfs -put $HADOOP_PREFIX/etc/hadoop/ input  
  
WORKDIR /usr/local/hadoop  
  
ADD bootstrap.sh /usr/local/src/bootstrap.sh  
RUN chown root:root /usr/local/src/bootstrap.sh  
RUN chmod 700 /usr/local/src/bootstrap.sh  
  
ENV HADOOP_BOOTSTRAP /usr/local/src/bootstrap.sh  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090 8020 9000  
# Mapred ports  
EXPOSE 10020 19888  
# Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
# Other ports  
EXPOSE 49707 2122  
ENTRYPOINT ["/usr/local/src/bootstrap.sh"]  

