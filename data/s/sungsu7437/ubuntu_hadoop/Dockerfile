FROM sungsu7437/ubuntu:16.04  
MAINTAINER sungsu7437  
  
USER root  
  
# install dev tools  
RUN apt-get install -y curl openssh-server openssh-client rsync wget  
  
# passwordless ssh  
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key
/root/.ssh/id_rsa  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# java  
RUN mkdir -p /usr/java/default && \  
curl -Ls 'http://download.oracle.com/otn-
pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz' -H 'Cookie:
oraclelicense=accept-securebackup-cookie' | \  
tar --strip-components=1 -xz -C /usr/java/default/  
  
ENV JAVA_HOME /usr/java/default/  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# hadoop  
RUN wget
http://ftp.daumkakao.com/apache/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz  
RUN tar -xvzf hadoop-2.6.0.tar.gz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.6.0 hadoop  
RUN rm hadoop-2.6.0.tar.gz  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV PATH $PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN mkdir -pv $HADOOP_PREFIX/input  
RUN mkdir -pv $HADOOP_PREFIX/dfs  
RUN mkdir -pv $HADOOP_PREFIX/dfs/name  
RUN mkdir -pv $HADOOP_PREFIX/dfs/data  
RUN mkdir -pv $HADOOP_PREFIX/tmp  
  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# pseudo distributed  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD core-site.xml $HADOOP_PREFIX/etc/hadoop/core-site.xml  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
ADD slaves $HADOOP_PREFIX/etc/hadoop/slaves  
  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
  
# fixing the libhadoop.so like a boss  
RUN rm /usr/local/hadoop/lib/native/*  
RUN wget http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.6.0.tar  
RUN tar xvf hadoop-native-64-2.6.0.tar -C /usr/local/hadoop/lib/native/  
RUN rm hadoop-native-64-2.6.0.tar  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
# # installing supervisord  
# RUN yum install -y python-setuptools  
# RUN easy_install pip  
# RUN curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -o
- | python  
# RUN pip install supervisor  
#  
# ADD supervisord.conf /etc/supervisord.conf  
# workingaround docker.io build error  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
#RUN service ssh start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -mkdir -p
/user/root  
#RUN service ssh start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -put
$HADOOP_PREFIX/etc/hadoop/ input  
COPY bootstrap.sh /etc/bootstrap.sh  
RUN chown root.root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030  
ENTRYPOINT ["/etc/bootstrap.sh"]  

