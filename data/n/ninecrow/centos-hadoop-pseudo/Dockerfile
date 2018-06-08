FROM ninecrow/centos7-oraclejdk:v1  
  
USER root  
  
RUN yum update -y; \  
yum install -y vim  
  
ENV HADOOP_VERSION 3.1.0  
ENV HADOOP_URL
https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz  
  
  
#tar -xzf *.gz -C /opt/ 静默方式解压  
RUN set -x \  
&& wget "$HADOOP_URL" -O /tmp/hadoop.tar.gz \  
&& tar -xzf /tmp/hadoop.tar.gz -C /opt/ \  
&& rm -f /tmp/hadoop.tar.gz  
#COPY hadoop-3.1.0.tar.gz /tmp/hadoop.tar.gz  
RUN ln -s /opt/hadoop-$HADOOP_VERSION /opt/hadoop  
RUN mkdir /opt/hadoop-$HADOOP_VERSION/logs  
RUN mkdir /hadoop-data  
  
ENV HADOOP_HOME /opt/hadoop  
ENV HADOOP_COMMON_HOME /opt/hadoop  
ENV HADOOP_HDFS_HOME /opt/hadoop  
ENV HADOOP_MAPRED_HOME /opt/hadoop  
ENV HADOOP_YARN_HOME /opt/hadoop  
ENV HADOOP_CONF_DIR /opt/hadoop/etc/hadoop  
ENV YARN_CONF_DIR $HADOOP_HOME/etc/hadoop  
  
#sed命令替换hadoop-env.sh中的环境变量的值  
RUN sed -i '/^#.export JAVA_HOME/ s:.*:export
JAVA_HOME=/opt/soft/java/jdk/jdk1.8.0_161\n:' $HADOOP_HOME/etc/hadoop/hadoop-
env.sh  
RUN sed -i '/^#.export HADOOP_HOME/ s:.*:export HADOOP_HOME=/opt/hadoop\n:'
$HADOOP_HOME/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^#.export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop\n:' $HADOOP_HOME/etc/hadoop/hadoop-
env.sh  
#添加用户配置，否则启动start-dfs.sh, start-yarn.sh 失败  
RUN sed -i '/^#.export HDFS_NAMENODE_USER/ s:.*:export
HDFS_NAMENODE_USER=root\nexport HDFS_DATANODE_USER=root\nexport
HDFS_SECONDARYNAMENODE_USER=root\nexport
YARN_RESOURCEMANAGER_USER=root\nexport YARN_NODEMANAGER_USER=root\n:'
$HADOOP_HOME/etc/hadoop/hadoop-env.sh  
  
#复制配置文件  
ADD core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml  
  
# 初始namenode , this is locally step 1;  
RUN $HADOOP_HOME/bin/hdfs namenode -format  
  
# If you cannot ssh to localhost without a passphrase, execute the following
commands  
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa  
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  
RUN chmod 0600 ~/.ssh/authorized_keys  
  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
  
  
CMD ["/etc/bootstrap.sh"]  
  
# Hdfs ports  
EXPOSE 50010 50020 50070 50075 50090  
# Mapred ports  
EXPOSE 19888  
#Yarn ports  
EXPOSE 8030 8031 8032 8033 8040 8042 8088  
#Other ports  
EXPOSE 49707 22  

