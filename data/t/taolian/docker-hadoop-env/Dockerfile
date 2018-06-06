# Create an distributed Hadoop cluster  
#  
# Environment  
## OS: CentOS 7.2.1511  
## JVM: Oracle JDK 1.8.102  
## CDH: 5.8.2  
FROM centos:7.2.1511  
MAINTAINER Tao Lian<liantao@me.com>  
  
USER root  
  
RUN env  
# Enable systemd  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
#Set Default docker command to init to start all enabled systemd services  
CMD ["/usr/sbin/init"]  
  
# Add Cloudera CDH 5  
ADD etc/yum.repos.d/cloudera-cdh5.repo /etc/yum.repos.d/cloudera-cdh5.repo  
RUN yum updateinfo  
## Install hdfs  
RUN yum install -y hadoop-hdfs-namenode hadoop-hdfs-secondarynamenode hadoop-
hdfs-datanode ; yum clean all  
## Install mapr  
RUN yum install -y hadoop-mapreduce hadoop-mapreduce-historyserver ; yum clean
all  
## Install YARN  
RUN yum install -y hadoop-yarn hadoop-yarn-resourcemanager hadoop-yarn-
nodemanager ; yum clean all  
## Install hbase  
RUN yum install -y hbase hbase-master hbase-regionserver ; yum clean all  
## Install zookeeper  
RUN yum install -y zookeeper-server zookeeper-native ; yum clean all  
  
## Optional management tools  
## RUN yum install -y hue-common hue-hbase hue-zookeeper hue-server hbase-
thrift  
RUN yum install -y net-tools wget openssh-server openssh-clients rsync ; yum
clean all  
RUN wget --quiet --no-cookies --no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.rpm"  
RUN yum install -y jdk-8u102-linux-x64.rpm ; yum clean all  
RUN rm -f jdk-8u102-linux-x64.rpm  
  
# Disabled unused services  
RUN systemctl disable postfix  
RUN systemctl disable sshd  
  
# Set environment variables.  
ENV JAVA_HOME=/usr/java/default  
ENV PATH=$PATH:$JAVA_HOME/bin  
  
ENV TERM=xterm  
  
# Disable IPv6  
RUN chmod +x /etc/rc.d/rc.local  
RUN echo "sysctl -w net.ipv6.conf.all.disable_ipv6=1" >> /etc/rc.d/rc.local  
RUN echo "sysctl -w net.ipv6.conf.default.disable_ipv6=1" >>
/etc/rc.d/rc.local  
RUN echo "sysctl -w net.ipv6.conf.lo.disable_ipv6=1" >> /etc/rc.d/rc.local

