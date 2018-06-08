From centos  
  
MAINTAINER Lich  
  
WORKDIR /root  
  
# if you have this file in local  
# COPY hadoop-2.8.1.tar.gz .  
# rpm -ivh https://repo.mysql.com//mysql57-community-release-el7-11.noarch.rpm
&& \ mysql mysql-serve  
RUN yum install wget openssh-server openssh-clients java-1.8.0-openjdk
java-1.8.0-openjdk-devel which r -y && \  
mkdir /docker-entrypoint-initdb.d && \  
wget
http://archive.apache.org/dist/hadoop/core/hadoop-2.8.1/hadoop-2.8.1.tar.gz &&
\  
tar -zxf hadoop-2.8.1.tar.gz && \  
mv hadoop-2.8.1 /usr/local/hadoop && \  
rm -rf hadoop-2.8.1.tar.gz && \  
rm -rf /usr/local/hadoop/share/doc && \  
wget http://archive.apache.org/dist/hbase/stable/hbase-1.2.6-bin.tar.gz && \  
tar -zxf hbase-1.2.6-bin.tar.gz && \  
mv hbase-1.2.6 /usr/local/hbase && \  
rm -rf hbase-1.2.6-bin.tar.gz && \  
rm -rf /usr/local/hbase/docs/ && \  
yum clean all  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ENV JAVA_HOME=/usr/lib/jvm/jre-openjdk  
ENV HADOOP_HOME=/usr/local/hadoop  
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin  
  
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N '' && \  
ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' && \  
ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N ''  
  
RUN mkdir -p ~/hdfs/namenode && \  
mkdir -p ~/hdfs/datanode && \  
mkdir $HADOOP_HOME/logs && \  
mkdir -p ~/zookeeper/data  
  
COPY config/* /tmp/  
  
RUN mv /tmp/ssh_config ~/.ssh/config && \  
mv /tmp/hadoop-env.sh /usr/local/hadoop/etc/hadoop/hadoop-env.sh && \  
mv /tmp/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml && \  
mv /tmp/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml && \  
mv /tmp/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml && \  
mv /tmp/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml && \  
mv /tmp/slaves $HADOOP_HOME/etc/hadoop/slaves && \  
mv /tmp/start-hadoop.sh ~/start-hadoop.sh && \  
mv /tmp/run-wordcount.sh ~/run-wordcount.sh && \  
mv /tmp/hbase-site.xml /usr/local/hbase/conf && \  
mv /tmp/regionservers /usr/local/hbase/conf && \  
mv /tmp/hbase-env.sh /usr/local/hbase/conf  
  
RUN chmod +x ~/start-hadoop.sh && \  
chmod +x ~/run-wordcount.sh && \  
chmod +x $HADOOP_HOME/sbin/start-dfs.sh && \  
chmod +x $HADOOP_HOME/sbin/start-yarn.sh  
  
WORKDIR /usr/local/hadoop/bin  
  
# format namenode  
RUN /usr/local/hadoop/bin/hdfs namenode -format  
  
WORKDIR /root  
CMD ["mysqld"]  
CMD [ "sh", "-c", "/usr/sbin/sshd -D;bash"]  

