FROM ingensi/hadoop-cdh-base:cdh5  
MAINTAINER Ingensi labs <contact@ingensi.com>  
  
# INSTALL PSEUDO DISTRIBUTED CDH  
RUN yum clean all \  
&& yum install -y hadoop-conf-pseudo  
  
# INSTALL SUPERVISORD  
RUN yum install -y python-setuptools \  
&& easy_install pip \  
&& pip install supervisor \  
&& mkdir /etc/supervisord.d/  
  
# ADD SUPERVISORD CONFS  
ADD files/supervisord.conf /etc/supervisord.conf  
ADD files/supervisord.d/* /etc/supervisord.d/  
  
# Add SUPERVISORD BOOTSTRAP SCRIPT  
ADD files/bootstrap.sh /root/bootstrap.sh  
RUN chmod +x /root/bootstrap.sh  
  
# ADD STARTUP SCRIPT  
ADD files/startup.sh /root/startup.sh  
ADD files/conf.sh /root/conf.sh  
RUN chmod +x /root/startup.sh  
  
# CREATE CONF DIRECTORIES  
RUN mkdir /tmp/hadoop_conf  
  
# HDFS PORTS  
EXPOSE 50010 1004 50075 1006 50020 8020 50070 50470  
# YARN PORTS  
EXPOSE 8032 8030 8031 8033 8088 8040 8042 8041 10020 19888  
CMD /root/startup.sh  

