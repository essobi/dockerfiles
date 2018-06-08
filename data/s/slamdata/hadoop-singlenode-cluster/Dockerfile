FROM java:8u111-jre  
  
COPY bin/wrapper_script.sh wrapper_script.sh  
ARG HADOOP_VERSION="2.7.3"  
RUN apt-get update && \  
apt-get -y install ssh  
  
RUN curl -L http://www-
us.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
| tar -xz -C /opt/  
  
# hadoop setup  
RUN mv /opt/hadoop-${HADOOP_VERSION} /opt/hadoop  
COPY conf/core-site.xml /opt/hadoop/etc/hadoop/  
COPY conf/hdfs-site.xml /opt/hadoop/etc/hadoop/  
COPY conf/slaves /opt/hadoop/etc/hadoop/  
COPY bin/hadoop.sh /etc/profile.d/  
RUN mkdir /opt/hadoop/logs  
  
RUN ssh-keygen -t rsa -P '' -f /root/.ssh/id_rsa  
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys  
RUN chmod 0600 /root/.ssh/authorized_keys  
  
RUN /opt/hadoop/bin/hdfs namenode -format  
RUN apt-get clean all  
  
EXPOSE 8030-8033 8088 9000 10020 19888 50010 50020 50070 50075 50090  
CMD ./wrapper_script.sh  

