# ---- xPatterns Hadoop Docker ----------------------------  
# ---- Version Control ------------------------------------  
FROM nimmis/java:oracle-8-jdk  
  
ENV HIVE_VERSION 1.2.1  
ENV XPATTERNS_WORKFLOW_LAUNCHER_VERSION 2.1.4  
ENV XPATTERNS_SPARK_BRIDGE_VERSION 2.0.7  
# ---- Download Links -------------------------------------  
ENV XPATTERNS_SPARK_BRIDGE_LINK xpatterns/spark-
bridge/${XPATTERNS_SPARK_BRIDGE_VERSION}/xpatterns-spark-
bridge-${XPATTERNS_SPARK_BRIDGE_VERSION}.jar  
ENV XPATTERNS_WORKFLOW_LAUNCHER_LINK
xpatterns/transformation/${XPATTERNS_WORKFLOW_LAUNCHER_VERSION}/tcomponent-
launcher-${XPATTERNS_WORKFLOW_LAUNCHER_VERSION}.jar  
ENV HIVE_DOWNLOAD_LINK
https://s3.amazonaws.com/xpatterns/dependencies/hive/apache-
hive-${HIVE_VERSION}-bin.tar.gz  
  
#Base image doesn't start in root  
WORKDIR /  
  
# ---- Default Environmental Variables --------------------  
ENV HIVE_HOME /usr/local/apache-hive-${HIVE_VERSION}-bin  
ENV WORKFLOW_HOME /opt/atigeo/workflow  
ENV SPARK_BRIDGE_DIR /opt/atigeo/spark-bridge  
  
# ---- apt-get install ------------------------------------  
RUN apt-get update && apt-get install -y wget zip  
  
# ---- Set the locale -------------------------------------  
RUN locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#Add the CDH 5 repository  
COPY conf/cloudera.list /etc/apt/sources.list.d/cloudera.list  
#Set preference for cloudera packages  
COPY conf/cloudera.pref /etc/apt/preferences.d/cloudera.pref  
#Add repository for python installation  
COPY conf/python.list /etc/apt/sources.list.d/python.list  
  
#Add a Repository Key  
RUN wget http://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh/archive.key
-O archive.key && sudo apt-key add archive.key && sudo apt-get update  
  
#Install CDH package and dependencies  
RUN sudo apt-get install -y zookeeper-
server=3.4.5+cdh5.4.4+91-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
RUN sudo apt-get install -y hadoop-conf-
pseudo=2.6.0+cdh5.4.4+597-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
RUN sudo apt-get install -y oozie=4.1.0+cdh5.4.4+145-1.cdh5.4.4.p0.6~trusty-
cdh5.4.4  
RUN sudo apt-get install -y python2.7=2.7.6-8ubuntu0.2  
RUN sudo apt-get install -y hue=3.7.0+cdh5.4.4+1236-1.cdh5.4.4.p0.6~trusty-
cdh5.4.4  
RUN sudo apt-get install -y hue-
plugins=3.7.0+cdh5.4.4+1236-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
RUN sudo apt-get install -y spark-
core=1.3.0+cdh5.4.4+41-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
RUN sudo apt-get install -y spark-history-
server=1.3.0+cdh5.4.4+41-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
RUN sudo apt-get install -y spark-
python=1.3.0+cdh5.4.4+41-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
  
#RUN sudo apt-get install -y hive=1.1.0+cdh5.4.4+157-1.cdh5.4.4.p0.6~trusty-
cdh5.4.4  
#RUN sudo apt-get install -y hive-
metastore=1.1.0+cdh5.4.4+157-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
#RUN sudo apt-get install -y hive-
server2=1.1.0+cdh5.4.4+157-1.cdh5.4.4.p0.6~trusty-cdh5.4.4  
RUN sudo apt-get install -y mysql-server  
  
RUN wget http://cdn.mysql.com//Downloads/Connector-J/mysql-connector-
java-5.1.37.tar.gz -P /tmp/  
RUN tar xzf /tmp/mysql-connector-java-5.1.37.tar.gz -C /tmp/  
RUN mv /tmp/mysql-connector-java-5.1.37/mysql-connector-java-5.1.37-bin.jar
/usr/lib/hive/lib/  
  
#RUN sudo apt-get install -y libmysql-java  
#RUN ln -s /usr/share/java/libmysql-java.jar /usr/lib/hive/lib/libmysql-
java.jar  
#Copy updated config files  
COPY conf/core-site.xml /etc/hadoop/conf/core-site.xml  
COPY conf/hdfs-site.xml /etc/hadoop/conf/hdfs-site.xml  
COPY conf/mapred-site.xml /etc/hadoop/conf/mapred-site.xml  
COPY conf/hadoop-env.sh /etc/hadoop/conf/hadoop-env.sh  
COPY conf/yarn-site.xml /etc/hadoop/conf/yarn-site.xml  
COPY conf/oozie-site.xml /etc/oozie/conf/oozie-site.xml  
COPY conf/spark-defaults.conf /etc/spark/conf/spark-defaults.conf  
COPY conf/hue.ini /etc/hue/conf/hue.ini  
COPY conf/hive-site-server.xml /etc/lib/hive/conf/hive-site.xml  
COPY conf/hive-site-meta.xml /usr/local/apache-hive-1.2.1-bin/conf/hive-
site.xml  
COPY conf/hive-site-meta.xml /etc/hive/conf.dist/hive-site.xml  
  
# ---- Install hive ---------------------------------------  
RUN wget ${HIVE_DOWNLOAD_LINK} -P /tmp/  
RUN tar xzf /tmp/apache-hive-${HIVE_VERSION}-bin.tar.gz -C /usr/local/  
#RUN mv /usr/lib/hive/conf/hive-env.sh.template /usr/lib/hive/conf/hive-env.sh  
# ---- Format HDFS ----------------------------------------  
#RUN sudo -u hdfs hdfs namenode -format  
RUN wget http://archive.cloudera.com/gplextras/misc/ext-2.2.zip -O ext.zip &&
\  
unzip ext.zip -d /var/lib/oozie  
  
#RUN service zookeeper-server init  
# ---- OpenSSH server -------------------------------------  
RUN apt-get update -y && apt-get install -y openssh-server  
  
RUN sudo -u oozie ssh-keygen -b 2048 -t rsa -f /var/lib/oozie/.ssh/id_rsa -q
-N ""  
RUN mkdir /root/.ssh/  
RUN cat /var/lib/oozie/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys  
RUN sed -i '/pam_loginuid/s/^/#/' /etc/pam.d/sshd  
  
# ---- Download xPatterns JARs ----------------------------  
RUN wget https://s3.amazonaws.com/${XPATTERNS_WORKFLOW_LAUNCHER_LINK} -P
${WORKFLOW_HOME}/bin/  
RUN wget https://s3.amazonaws.com/${XPATTERNS_SPARK_BRIDGE_LINK} -P
${SPARK_BRIDGE_DIR}/  
  
# ---- Ports ----------------------------------------------  
# NameNode (HDFS)  
EXPOSE 8020 50070  
# DataNode (HDFS)  
EXPOSE 50010 50020 50075  
# ResourceManager (YARN)  
EXPOSE 8030 8031 8032 8033 8088  
# NodeManager (YARN)  
EXPOSE 8040 8042  
# JobHistoryServer  
EXPOSE 10020 19888  
# Hue  
EXPOSE 8888  
# Spark history server  
EXPOSE 18080  
# Technical port which can be used for your custom purpose.  
EXPOSE 9999  
# Hive Metastore  
EXPOSE 9083  
# ---- Setup run script -----------------------------------  
COPY conf/run.sh /usr/bin/run.sh  
RUN chmod u+x /usr/bin/run.sh  
CMD ["/usr/bin/run.sh"]  

