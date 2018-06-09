from stackbrew/ubuntu:saucy  
MAINTAINER Radoslaw Stankiewicz <rrydziu@gmail.com>  
  
WORKDIR /root/  
  
# Install package with add-apt-repository  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Enable Ubuntu repositories  
RUN add-apt-repository -y multiverse && \  
add-apt-repository -y restricted && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && apt-get upgrade -y  
  
# Install latest Oracle Java from PPA  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer oracle-java7-set-default  
  
# Install SSH server and Zookeeper  
RUN apt-get install -y ant openssh-server zookeeperd vim telnet  
  
# Download Hadoop  
RUN wget -q
'http://archive.apache.org/dist/hadoop/core/hadoop-0.20.204.0/hadoop-0.20.204.0-bin.tar.gz'  
RUN wget -q
'http://archive.apache.org/dist/hbase/hbase-0.90.4/hbase-0.90.4.tar.gz'  
RUN wget -q
'http://ftp.piotrkosoft.net/pub/mirrors/ftp.apache.org/nutch/2.2.1/apache-
nutch-2.2.1-src.tar.gz'  
# Install util packages  
RUN apt-get install -y rsync curl  
  
# Setup system user and group to own and run Hadoop  
RUN addgroup hadoop && adduser --ingroup hadoop hduser  
RUN usermod -a -G hadoop zookeeper  
  
# Setup SSH keys for Hadoop  
RUN su -l -c 'ssh-keygen -t rsa -f /home/hduser/.ssh/id_rsa -P ""' hduser && \  
cat /home/hduser/.ssh/id_rsa.pub | su -l -c 'tee -a
/home/hduser/.ssh/authorized_keys' hduser  
ADD config/ssh-config /home/hduser/.ssh/config  
RUN chmod 600 /home/hduser/.ssh/config  
RUN chown hduser /home/hduser/.ssh/config  
  
# Fix Ubuntu 13.10 SSH daemon problem with docker:
http://docs.docker.io/en/latest/examples/running_ssh_service/  
RUN sed -ri 's/session[[:blank:]]+required[[:blank:]]+pam_loginuid.so/session
optional pam_loginuid.so/g' /etc/pam.d/sshd  
  
# Deploy and setup file permissions  
RUN tar xvfz /root/hadoop-0.20.204.0-bin.tar.gz -C /opt && \  
ln -s /opt/hadoop-0.20.204.0 /opt/hadoop && \  
chown -R root:root /opt/hadoop-0.20.204.0 && \  
mkdir /opt/hadoop-0.20.204.0/logs && \  
chown -R hduser:hadoop /opt/hadoop-0.20.204.0/logs  
  
# Deploy and setup file permissions  
RUN tar xvfz /root/hbase-0.90.4.tar.gz -C /opt && \  
ln -s /opt/hbase-0.90.4 /opt/hbase && \  
chown -R root:root /opt/hbase-0.90.4 && \  
mkdir /opt/hbase-0.90.4/logs && \  
chown -R hduser:hadoop /opt/hbase-0.90.4/logs  
  
# Deploy and setup file permissions  
RUN tar xvfz /root/apache-nutch-2.2.1-src.tar.gz -C /opt && \  
chown -R root:root /opt/apache-nutch-2.2.1 && \  
mkdir /opt/apache-nutch-2.2.1/logs && \  
chown -R hduser:hadoop /opt/apache-nutch-2.2.1/logs  
  
# Setup hduser environment  
ADD config/bashrc /home/hduser/.bashrc  
  
# Configure Hadoop  
ADD config/core-site.xml /tmp/hadoop-etc/core-site.xml  
ADD config/mapred-site.xml /tmp/hadoop-etc/mapred-site.xml  
ADD config/hdfs-site.xml /tmp/hadoop-etc/hdfs-site.xml  
  
ADD config/hbase-site.xml /tmp/hbase-etc/hbase-site.xml  
ADD config/nutch-site.xml /tmp/nutch-etc/nutch-site.xml  
RUN cp /tmp/hadoop-etc/* /opt/hadoop/conf/  
RUN mv /tmp/hadoop-etc/* /opt/hadoop/etc/hadoop  
RUN mv /tmp/hbase-etc/* /opt/hbase/conf/  
RUN mv /tmp/nutch-etc/* /opt/apache-nutch-2.2.1/conf/  
  
RUN rm /opt/hbase/lib/hadoop-core* && cp /opt/hadoop/hadoop-core*
/opt/hadoop/lib/commons-configuration* /opt/hbase/lib/  
  
ENV NUTCH_ROOT /opt/apache-nutch-2.2.1  
RUN echo 'gora.datastore.default=org.apache.gora.hbase.store.HBaseStore' >>
/opt/apache-nutch-2.2.1/conf/gora.properties  
RUN vim -c 'g/name="gora-hbase"/+1d' -c 'x' $NUTCH_ROOT/ivy/ivy.xml  
RUN vim -c 'g/name="gora-hbase"/-1d' -c 'x' $NUTCH_ROOT/ivy/ivy.xml  
RUN cd $NUTCH_ROOT && ant runtime  
RUN ln -s /opt/apache-nutch-2.2.1/runtime/local /opt/nutch  
ENV NUTCH_HOME /opt/nutch  
ENV HADOOP_HOME /opt/hadoop  
ENV NUTCHSERVER_PORT 8899  
# NUTCH  
EXPOSE 8899  
# Expose SSHD  
EXPOSE 22  
# QuorumPeerMain (Zookeeper)  
EXPOSE 2181 39534  
# NameNode (HDFS)  
EXPOSE 8020 50070 9000  
# DataNode (HDFS)  
EXPOSE 50010 50020 50075  
# SecondaryNameNode (HDFS)  
EXPOSE 50090  
# Trackers  
EXPOSE 50030 50060  
#HBASE  
EXPOSE 6000 60010 60020 60030  
# Thrift  
EXPOSE 9090 9095  
# Create start script  
ADD config/run-hadoop.sh /root/run-hadoop.sh  
RUN chmod +x /root/run-hadoop.sh  
  
CMD ["/root/run-hadoop.sh"]  

