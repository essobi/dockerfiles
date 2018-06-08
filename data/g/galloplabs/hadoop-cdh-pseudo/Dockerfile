FROM galloplabs/hadoop-cdh-base  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
# INSTALL PSEUDO DISTRIBUTED CDH  
RUN yum install -y hadoop-conf-pseudo  
  
# INSTALL SPARK  
RUN yum install -y spark-core spark-python  
  
# INSTALL SUPERVISORD  
RUN yum install -y python-setuptools \  
&& easy_install pip \  
&& pip install supervisor \  
&& mkdir /etc/supervisord.d/  
  
# ADD SUPERVISORD CONFS  
ADD files/supervisord.conf /etc/supervisord.conf  
ADD files/supervisord.d/* /etc/supervisord.d/  
  
# ADD SCRIPTS  
ADD files/startup.sh /root/startup.sh  
ADD files/run.sh /root/run.sh  
  
# ADD HADOOP ENVS  
ADD files/hadoop-env.sh /etc/hadoop/conf/hadoop-env.sh  
  
# ADD YARN CONFIG  
ADD files/yarn-site.xml /etc/hadoop/conf/yarn-site.xml  
  
# CREATE CONF DIRECTORIES  
RUN mkdir /tmp/hadoop_conf  
  
# DEFAULT STARTUP ENVS  
ENV FORMAT_HDFS=true  
ENV INITIALIZE_HDFS=true  
  
# HDFS PORTS  
EXPOSE 50010 1004 50075 1006 50020 8020 50070 50470  
# YARN PORTS  
EXPOSE 8032 8030 8031 8033 8088 8040 8042 8041 10020 19888  
CMD /root/startup.sh  

