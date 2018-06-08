FROM centos:centos6  
MAINTAINER Yogesh Pandit  
  
USER root  
  
WORKDIR /tmp  
ADD scripts/* /tmp/  
  
RUN yum -y update; yum clean all  
  
# Install prerequisites  
RUN yum install -y curl which tar sudo htop openssh-server openssh-clients
automake autoconf gcc-c++ m4 perl git libtool libevent-devel zlib-devel
openssl-devel openssl wget git mysql-server mysql mysql-connector-java python-
devel mysql-devel sqlite-devel libxml2-devel libxslt-devel epel-release
openldap-clients openldap-servers vim; yum update -y libselinux; yum -y
update; yum -y install nginx; yum clean all  
RUN service mysqld start; chkconfig mysqld on  
  
# Passwordless SSH  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key; ssh-keygen -q -N
"" -t rsa -f /etc/ssh/ssh_host_rsa_key; ssh-keygen -q -N "" -t rsa -f
/root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
RUN service sshd start; chkconfig sshd on  
  
# Install Java  
RUN cd /tmp; wget http://www-lry.ciril.net/client/java/jdk-7u75-linux-x64.rpm  
RUN rpm -Uh /tmp/jdk-7u75-linux-x64.rpm; rm /tmp/jdk-7u75-linux-x64.rpm  
  
# Set JAVA_HOME and PATH  
ENV JAVA_HOME /usr/java/latest  
ENV PATH $JAVA_HOME/bin:$PATH  
RUN echo -e "export JAVA_HOME=/usr/java/latest\nexport
PATH=$JAVA_HOME/bin:$PATH" > /etc/profile.d/java.sh; source
/etc/profile.d/java.sh  
  
# Setup Hortonworks HDP 2.1  
RUN wget -nv http://public-
repo-1.hortonworks.com/HDP/centos6/2.x/updates/2.1.10.0/hdp.repo -O
/etc/yum.repos.d/hdp.repo  
RUN yum repolist  
RUN yum install -y hadoop hadoop-hdfs hadoop-libhdfs hive hive-metastore
hadoop-yarn hadoop-mapreduce hadoop-client hbase  
# RUN yum install -y snappy snappy-devel lzo lzo-devel hadoop-lzo hadoop-lzo-
native  
# Set required environment variables  
ENV HADOOP_CONF_DIR /etc/hadoop/conf  
ENV HADOOP_HOME /usr/lib/hadoop  
ENV HADOOP_PREFIX /usr/lib/hadoop  
ENV HADOOP_LOG_DIR /var/log/hadoop  
ENV HIVE_CONF_DIR /etc/hive/conf  
ENV SPARK_HOME /usr/lib/spark/1.3.1  
# Install maven, spark, thrift, protobuf  
RUN sh /tmp/install.sh  
  
# Configure hadoop, hive-metastore  
RUN sh /tmp/configure.sh  
  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh; chmod 700 /etc/bootstrap.sh  
  
RUN rm /tmp/install.sh; rm /tmp/configure.sh  
  
# Expose HDFS/Hadoop ports  
EXPOSE 50020 50090 50070 50010 8020  
# Expose Apache Spark ports  
EXPOSE 18080 18081 7077  
CMD ["/etc/bootstrap.sh", "-bash"]  

