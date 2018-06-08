# Creates pseudo distributed hadoop 2.5.2  
#  
# docker build -t sequenceiq/hadoop .  
FROM centos:6.7  
MAINTAINER H2COMM  
  
USER root  
  
#curl -o “CentOS6-Base.repo”
http://mirrors.163.com/.help/CentOS6-Base-163.repo  
# COPY CentOS-Base.repo /etc/yum.repos.d/  
# install dev tools  
RUN yum install -y which tar sudo openssh-server openssh-clients rsync  
RUN yum update -y libselinux  
# passwordless ssh  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
# java  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm' -H 'Cookie:
oraclelicense=accept-securebackup-cookie'  
#COPY jdk-7u71-linux-x64.rpm /tmp/  
#RUN rpm -i /tmp/jdk-7u71-linux-x64.rpm  
#RUN rm /tmp/jdk-7u71-linux-x64.rpm  
RUN rpm -i jdk-7u51-linux-x64.rpm  
RUN rm jdk-7u51-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# hadoop  
RUN curl -s
http://www.eu.apache.org/dist/hadoop/common/hadoop-2.5.2/hadoop-2.5.2.tar.gz |
tar -xz -C /usr/local/  
  
#COPY hadoop-2.5.2.tar.gz /tmp/  
#RUN tar -xzf /tmp/hadoop-2.5.2.tar.gz -C /usr/local/  
RUN cd /usr/local && ln -s ./hadoop-2.5.2 hadoop  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV HADOOP_COMMON_HOME /usr/local/hadoop  
ENV HADOOP_HDFS_HOME /usr/local/hadoop  
ENV HADOOP_MAPRED_HOME /usr/local/hadoop  
ENV HADOOP_YARN_HOME /usr/local/hadoop  
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
  
RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/java/default\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport
HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN . $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
RUN mkdir $HADOOP_PREFIX/input  
RUN cp $HADOOP_PREFIX/etc/hadoop/*.xml $HADOOP_PREFIX/input  
  
# pseudo distributed  
ADD core-site.xml $HADOOP_PREFIX/etc/hadoop/core-site.xml  
#RUN sed s/HOSTNAME/localhost/ /usr/local/hadoop/etc/hadoop/core-
site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
RUN $HADOOP_PREFIX/bin/hdfs namenode -format  
#RUN $HADOOP_PREFIX/bin/hdfs datanode -format  
# fixing the libhadoop.so like a boss  
RUN rm /usr/local/hadoop/lib/native/*  
  
RUN curl -Ls http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.5.2.tar|tar -xz -C /usr/local/hadoop/lib/native/  
#COPY hadoop-native-64-2.5.2.tar /tmp/  
#RUN tar -xf /tmp/hadoop-native-64-2.5.2.tar -C /usr/local/hadoop/lib/native/  
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
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
# workingaround docker.io build error  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
RUN ls -la /usr/local/hadoop/etc/hadoop/*-env.sh  
  
# fix the 254 error code  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
RUN echo "Port 2122" >> /etc/ssh/sshd_config  
  
#RUN service sshd start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -mkdir -p
/user/root  
#RUN service sshd start && $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh &&
$HADOOP_PREFIX/sbin/start-dfs.sh && $HADOOP_PREFIX/bin/hdfs dfs -put
$HADOOP_PREFIX/etc/hadoop/ input  
COPY hosts /tmp/  
COPY slaves /usr/local/hadoop/etc/hadoop/  
  
#HIVE apache-hive-1.2.1-bin.tar.gz  
RUN curl -o /tmp/apache-hive-1.2.1-bin.tar.gz
http://apache.fayea.com/hive/hive-1.2.1/apache-hive-1.2.1-bin.tar.gz  
#COPY apache-hive-1.2.1-bin.tar.gz /tmp/  
RUN tar -xf /tmp/apache-hive-1.2.1-bin.tar.gz -C /usr/local/  
RUN mv /usr/local/apache-hive-1.2.1-bin /usr/local/hive  
ENV HIVE_HOME /usr/local/hive  
ENV PATH $PATH:$HIVE_HOME/bin  
ENV HIVE_CONF_DIR /usr/local/hive/conf  
COPY hive-site.xml /usr/local/hive/conf/  
COPY mysql-connector-java-5.1.38-bin.jar /usr/local/hive/lib/  
RUN cp /usr/local/hive/lib/jline-2.12.jar
/usr/local/hadoop-2.5.2/share/hadoop/yarn/lib/jline-0.9.94.jar  
RUN rm -f /tmp/*.gz /tmp/*.tar  
CMD ["/etc/bootstrap.sh", "-d"]  
  

