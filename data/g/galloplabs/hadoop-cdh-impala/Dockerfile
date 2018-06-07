FROM galloplabs/hadoop-cdh-pseudo  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
# INSTALL IMPALA  
RUN yum install -y impala impala-shell impala-server impala-catalog impala-
state-store  
  
# ADD SUPERVISORD CONFS  
ADD files/supervisord.d/* /etc/supervisord.d/  
  
# ADD SCRIPTS  
ADD files/startup.sh /root/startup.sh  
ADD files/run.sh /root/run.sh  
  
# DEFAULT STARTUP ENVS  
ENV FORMAT_HDFS=true  
ENV INITIALIZE_HDFS=true  
  
# HDFS PORTS  
EXPOSE 50010 1004 50075 1006 50020 8020 50070 50470  
# YARN PORTS  
EXPOSE 8032 8030 8031 8033 8088 8040 8042 8041 10020 19888  
# IMPALA PORTS  
EXPOSE 21000 21050 25000 25010 25020  
CMD /root/startup.sh  

