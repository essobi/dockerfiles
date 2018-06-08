FROM java:7  
MAINTAINER Elton Stoneman <elton@sixeyed.com>  
  
ENV JAVA_HOME=/usr  
ENV HADOOP_HOME=/opt/hadoop  
  
RUN mkdir /hadoop-setup  
WORKDIR /hadoop-setup  
  
ADD install-hadoop.sh /hadoop-setup/  
RUN chmod +x ./install-hadoop.sh  
RUN ./install-hadoop.sh  
ADD ./conf /opt/hadoop/etc/hadoop/  
  
ADD ./ssh/ssh.config /root/.ssh/config  
ADD ./ssh/setup-ssh.sh /hadoop-setup/  
RUN chmod +x ./setup-ssh.sh  
RUN ./setup-ssh.sh  
  
ADD setup-hdfs.sh /hadoop-setup/  
RUN chmod +x ./setup-hdfs.sh  
RUN ./setup-hdfs.sh  
  
# HDFS  
EXPOSE 50010 50020 50070 50075 50090 8020 9000  
# MapReduce UI  
EXPOSE 19888  
# YARN  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
ENV PATH=$PATH:/opt/hadoop/bin  
  
# run servers:  
ADD start-servers.sh /opt/hadoop/bin/  
RUN chmod +x /opt/hadoop/bin/start-servers.sh  
CMD /opt/hadoop/bin/start-servers.sh

