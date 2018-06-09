FROM centos:7  
  
MAINTAINER Swapnil Jain <swapnil@linux.com>  
LABEL description="Cloudera Hadoop 5.9 Base Docker Image"  
  
RUN yum -y install epel-release java-1.8.0-openjdk-devel && rm -rf
/var/cache/yum/* && yum clean all  
ENV JAVA_HOME /usr/lib/jvm/java-openjdk  
COPY cloudera-cdh.repo /etc/yum.repos.d  
RUN yum -y install hadoop supervisor && rm -rf /var/cache/yum/* && yum clean
all  
ENV CDH_VER 5.9  
COPY conf.d/* /usr/lib/hadoop/etc/hadoop/  
ENV HADOOP_HOME /usr/lib/hadoop  
ENV HADOOP_CONF_DIR /etc/hadoop/conf  
ENV HADOOP_COMMON_HOME /usr/lib/hadoop  
ENV HADOOP_HDFS_HOME /usr/lib/hadoop-hdfs  
ENV HADOOP_YARN_HOME /usr/lib/hadoop-yarn  
ENV HADOOP_MAPRED_HOME /usr/lib/hadoop-mapreduce  
CMD ["hadoop", "version"]  

