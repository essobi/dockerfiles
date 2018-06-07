FROM ubuntu:16.04  
MAINTAINER Dongjoon Hyun <dongjoon@apache.org>  
  
RUN apt-get update && apt-get install -y git curl unzip openssh-server python-
software-properties software-properties-common protobuf-compiler build-
essential python-dev  
  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN echo 'StrictHostKeyChecking no' > /root/.ssh/config  
RUN chmod 400 /root/.ssh/config  
COPY start.sh /root/  
COPY sync-hosts.sh /root/  
  
# java  
RUN apt-get install -y openjdk-8-jdk && rm -rf /var/lib/apt/lists/*  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN echo 'JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"' >> /etc/environment  
  
# elasticsearch  
RUN \  
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -
&& \  
echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" |
tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list && \  
apt-get update && apt-get install elasticsearch && \  
rm -rf /var/lib/apt/lists/*  
RUN \  
mkdir /usr/share/elasticsearch/config/ && \  
mkdir /data1 && \  
chown -R elasticsearch:elasticsearch /usr/share/elasticsearch /data1  
COPY elasticsearch.yml /etc/elasticsearch/  
COPY run-es.sh /root/  
  
# hadoop  
RUN \  
cd /usr/local && wget -q
http://www.us.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
&& \  
tar -xzf hadoop-2.7.3.tar.gz && \  
ln -s ./hadoop-2.7.3 hadoop && \  
rm hadoop-2.7.3.tar.gz  
  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV YARN_CONF_DIR /usr/local/hadoop/etc/hadoop  
RUN \  
echo 'HADOOP_PREFIX="/usr/local/hadoop"' >> /etc/environment && \  
echo 'HADOOP_COMMON_HOME="/usr/local/hadoop"' >> /etc/environment && \  
echo 'HADOOP_HDFS_HOME="/usr/local/hadoop"' >> /etc/environment && \  
echo 'HADOOP_MAPRED_HOME="/usr/local/hadoop"' >> /etc/environment && \  
echo 'HADOOP_YARN_HOME="/usr/local/hadoop"' >> /etc/environment && \  
echo 'HADOOP_CONF_DIR="/usr/local/hadoop/etc/hadoop"' >> /etc/environment && \  
echo 'YARN_CONF_DIR="/usr/local/hadoop/etc/hadoop"' >> /etc/environment  
  
RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=$JAVA_HOME\nexport
HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
  
COPY core-site.xml $HADOOP_PREFIX/etc/hadoop/  
COPY hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/  
COPY mapred-site.xml $HADOOP_PREFIX/etc/hadoop/  
COPY yarn-site.xml $HADOOP_PREFIX/etc/hadoop/  
  
RUN chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh  
COPY init-nn.sh /root/  
  
# spark  
RUN \  
cd /usr/local && wget -q
http://www.us.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.7.tgz
&& \  
tar -xzf spark-2.1.0-bin-hadoop2.7.tgz && \  
ln -s spark-2.1.0-bin-hadoop2.7 spark && \  
rm spark-2.1.0-bin-hadoop2.7.tgz  
  
ENV SPARK_HOME /usr/local/spark  
RUN echo 'SPARK_HOME="/usr/local/spark"' >> /etc/environment  
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin  
  
# ipython  
RUN \  
wget -qO- https://bootstrap.pypa.io/ez_setup.py | python2.7 && \  
easy_install-2.7 pip && \  
pip2.7 install --no-cache-dir "ipython[notebook]"  
  
# ipython notebook  
RUN \  
jupyter notebook --generate-config && \  
sed "s@# c.NotebookApp.ip = 'localhost'@c.NotebookApp.ip = '*'@g" -i
/root/.jupyter/jupyter_notebook_config.py && \  
ipython profile create pyspark  
COPY run-ipython-notebook.sh /root/  
COPY sample_python.ipynb /root/  
  
# hive  
RUN \  
cd /usr/local && wget -q http://www.us.apache.org/dist/hive/hive-2.1.1/apache-
hive-2.1.1-bin.tar.gz && \  
tar -xzf apache-hive-2.1.1-bin.tar.gz && \  
ln -s apache-hive-2.1.1-bin hive && \  
rm apache-hive-2.1.1-bin.tar.gz  
  
ENV HIVE_HOME /usr/local/hive  
ENV HADOOP_USER_CLASSPATH_FIRST true  
RUN \  
echo 'HIVE_HOME="/usr/local/hive"' >> /etc/environment && \  
echo 'HADOOP_USER_CLASSPATH_FIRST="true"' >> /etc/environment  
ENV PATH $PATH:$HIVE_HOME/bin  
COPY data.csv /root/  
COPY test-hive.sh /root/  
  
EXPOSE 22 4040 7077 8020 8030 8031 8032 8033 8040 8042 8080 8088 8888 9200
9300 10000 50010 50020 50060 50070 50075 50090  

