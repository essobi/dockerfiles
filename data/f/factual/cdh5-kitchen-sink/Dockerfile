FROM nimmis/java:openjdk-8-jdk  
MAINTAINER Martin Chalupa <chalimartines@gmail.com>  
  
#Base image doesn't start in root  
WORKDIR /  
  
#Add the CDH 5 repository  
COPY conf/cloudera.list /etc/apt/sources.list.d/cloudera.list  
#Set preference for cloudera packages  
COPY conf/cloudera.pref /etc/apt/preferences.d/cloudera.pref  
#Add repository for python installation  
COPY conf/python.list /etc/apt/sources.list.d/python.list  
  
# Add a Repository Key and Install CDH packages and deps  
RUN wget http://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh/archive.key
-O archive.key && \  
apt-key add archive.key && \  
apt-get update && \  
apt-get install -y zookeeper-server hadoop-conf-pseudo hbase-master hbase-
regionserver maven krb5-user krb5-kdc krb5-admin-server  
RUN wget
'http://mirror.metrocast.net/apache/spark/spark-2.2.1/spark-2.2.1-bin-
hadoop2.6.tgz' && tar -xzvf spark-2.2.1-bin-hadoop2.6.tgz && rm
spark-2.2.1-bin-hadoop2.6.tgz  
COPY conf/spark/* spark-2.2.1-bin-hadoop2.6/conf/  
# Install Kafka  
RUN useradd -m -U kafka && \  
mkdir -p /data/kafka/queues && \  
chown -R kafka /data/kafka && \  
rm -rf /usr/local/lib/kafka && \  
wget https://archive.apache.org/dist/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz && \  
tar xvzf kafka_2.11-0.9.0.1.tgz -C /usr/local/lib && \  
mv /usr/local/lib/kafka_2.11-0.9.0.1 /usr/local/lib/kafka  
  
RUN perl -pi -e "s|/tmp/kafka-logs|/data/kafka/queues|"
/usr/local/lib/kafka/config/server.properties  
RUN perl -pi -e "s|num.network.threads=3|num.network.threads=1|"
/usr/local/lib/kafka/config/server.properties  
RUN perl -pi -e "s|num.io.threads=8|num.io.threads=1|"
/usr/local/lib/kafka/config/server.properties  
RUN perl -pi -e
"s|socket.send.buffer.bytes=102400|socket.send.buffer.bytes=1024|"
/usr/local/lib/kafka/config/server.properties  
RUN perl -pi -e
"s|socket.receive.buffer.bytes=102400|socket.receive.buffer.bytes=1024|"
/usr/local/lib/kafka/config/server.properties  
RUN perl -pi -e
"s|zookeeper.connect=127.0.0.1:2181|zookeeper.connect=localhost:2181|"
/usr/local/lib/kafka/config/consumer.properties  
  
COPY scripts/init-kafka.sh /etc/init.d/  
  
#tweak launch wait times  
RUN perl -pi -e "s|sleep.*||" /usr/lib/hadoop/sbin/hadoop-daemon.sh  
  
#Copy updated config files  
COPY conf/core-site.xml /etc/hadoop/conf/core-site.xml  
COPY conf/hdfs-site.xml /etc/hadoop/conf/hdfs-site.xml  
COPY conf/mapred-site.xml /etc/hadoop/conf/mapred-site.xml  
COPY conf/hadoop-env.sh /etc/hadoop/conf/hadoop-env.sh  
COPY conf/yarn-site.xml /etc/hadoop/conf/yarn-site.xml  
COPY conf/hbase-site.xml /etc/hbase/conf/hbase-site.xml  
COPY conf/hbase-site.xml /etc/hadoop/conf/hbase-site.xml  
COPY conf/zoo.cfg /etc/zookeeper/conf/zoo.cfg  
COPY conf/jaas.conf /etc/zookeeper/conf/jaas.conf  
COPY conf/java.env /etc/zookeeper/conf/java.env  
COPY conf/hbase-zk-jaas.conf /etc/hbase/conf/zk-jaas.conf  
COPY conf/container-executor.cfg /etc/hadoop/conf/container-executor.cfg  
RUN chmod 644 /etc/hadoop/conf/container-executor.cfg  
  
#Add some hbase env variables...  
RUN echo 'export HBASE_OPTS="$HBASE_OPTS
-Djava.security.auth.login.config=/etc/hbase/conf/zk-jaas.conf"' >>
/etc/hbase/conf/hbase-env.sh  
RUN echo "export HBASE_MANAGES_ZK=false" >> /etc/hbase/conf/hbase-env.sh  
  
#copy kdc configs  
COPY conf/krb5.conf /etc/krb5.conf  
COPY conf/kdc.conf /etc/krb5kdc/kdc.conf  
COPY data/principal /etc/krb5kdc/principal  
COPY data/principal.kadm5 /etc/krb5kdc/principal.kadm5  
COPY data/principal.kadm5.lock /etc/krb5kdc/principal.kadm5.lock  
COPY data/principal.ok /etc/krb5kdc/principal.ok  
COPY data/stash /etc/krb5kdc/stash  
COPY scripts/init_krb.sh /usr/bin/init_krb.sh  
  
#some ZK stuff  
COPY conf/test-service-zk-jaas.conf /test-service-zk-jaas.conf  
COPY conf/test-user-zk-jaas.conf /test-user-zk-jaas.conf  
  
#Format HDFS  
#RUN sudo -u hdfs hdfs namenode -format  
#Copy launch script  
COPY scripts/run-hadoop.sh /usr/bin/run-hadoop.sh  
RUN chmod +x /usr/bin/run-hadoop.sh  
  
#Copy other scripts  
COPY scripts/runAs.sh /usr/bin/runAs.sh  
COPY scripts/killServices.sh /usr/bin/killServices.sh  
RUN chmod +x /usr/bin/runAs.sh  
RUN chmod +x /usr/bin/killServices.sh  
  
#fix some terminal preferences  
RUN echo export TERM=xterm >> /etc/bash.bashrc  
  
# get support jar from github  
RUN wget -O /cdh5-docker-support.jar https://github.com/factual/docker-
cdh5-kitchen-sink/releases/download/1.1.0/cdh5-docker-
support-1.1.0-SNAPSHOT.jar  
# if you are doing testing, you can retrieve the support jar from a local
build  
#COPY ./support/target/cdh5-docker-support-1.1.0-SNAPSHOT.jar /cdh5-docker-
support.jar  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
HADOOP_COMMON_HOME=/usr/lib/hadoop \  
HADOOP_HDFS_HOME=/usr/lib/hadoop-hdfs \  
HADOOP_MAPRED_HOME=/usr/lib/hadoop-mapreduce \  
HADOOP_YARN_HOME=/usr/lib/hadoop-yarn  
  
# NameNode (HDFS)  
EXPOSE \  
# NameNode (HDFS)  
8020 50070 \  
# Datanode (HDFS)  
50010 50020 50075 \  
# ResourceManager (YARN)  
8030 8031 8032 8033 8088 \  
# NodeManager (YARN)  
8040 8042 \  
# JobHistoryServer  
10020 19888 \  
#HBASE MASTER  
60010 \  
# Technical port which can be used for your custom purpose.  
9999  
# Run startup script  
CMD /usr/bin/run-hadoop.sh | tee /var/log/startup.log  

