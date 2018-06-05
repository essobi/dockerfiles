FROM joegagliardo/ubuntu  
MAINTAINER joegagliardo  
  
# As much as possible I am trying to put as many steps in a single RUN command
to minimize  
# the ultimate build size. I also prefer to echo a file and build it in a RUN
so there is  
# no reliance on outside files needed if you use an ADD  
# This section is an easy place to change the desired password and versions
you want to install  
  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030 3306 10000 10001 10002  
  
# MYSQL Passwords  
ARG HIVEUSER_PASSWORD=hivepassword  
ARG HIVE_METASTORE=hivemetastore  
  
ADD examples /examples  
ADD datasets /examples  
ADD conf /conf  
ADD scripts /scripts  
# Versions  
ARG HADOOP_VERSION=2.9.0  
ARG PIG_VERSION=0.17.0  
ARG HIVE_VERSION=2.3.3  
ARG SPARK_VERSION=2.3.0  
ARG ZOOKEEPER_VERSION=3.4.11  
ARG HBASE_VERSION=1.4.3  
ARG MONGO_VERSION=3.6.3  
ARG MONGO_JAVA_DRIVER_VERSION=3.6.3  
ARG MONGO_HADOOP_VERSION=2.0.2  
ARG CASSANDRA_VERSION=311  
ARG SPARK_CASSANDRA_VERSION=2.0.7-s_2.11  
ARG COCKROACH_VERSION=2.0.0  
  
# Download URLs  
ARG HADOOP_BASE_URL=http://mirrors.sonic.net/apache/hadoop/common  
ARG
HADOOP_URL=${HADOOP_BASE_URL}/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz  
  
ARG PIG_BASE_URL=http://apache.claz.org/pig  
ARG PIG_URL=${PIG_BASE_URL}/pig-${PIG_VERSION}/pig-${PIG_VERSION}.tar.gz  
  
ARG HIVE_BASE_URL=http://apache.claz.org/hive  
ARG HIVE_URL=${HIVE_BASE_URL}/hive-${HIVE_VERSION}/apache-
hive-${HIVE_VERSION}-bin.tar.gz  
  
ARG SPARK_BASE_URL=http://apache.claz.org/spark  
ARG
SPARK_URL=${SPARK_BASE_URL}/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop2.7.tgz  
  
ARG ZOOKEEPER_BASE_URL=http://apache.claz.org/zookeeper/  
ARG
ZOOKEEPER_URL=${ZOOKEEPER_BASE_URL}/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz  
  
ARG HBASE_BASE_URL=http://apache.mirrors.pair.com/hbase  
ARG
HBASE_URL=${HBASE_BASE_URL}/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz  
  
ARG MONGO_BASE_URL=https://fastdl.mongodb.org/linux  
ARG MONGO_URL=${MONGO_BASE_URL}/mongodb-linux-x86_64-${MONGO_VERSION}.tgz  
  
ARG MONGO_JAVA_DRIVER_BASE_URL=https://repo1.maven.org/maven2/org/mongodb  
ARG MONGO_JAVA_DRIVER_URL=${MONGO_JAVA_DRIVER_BASE_URL}/mongo-java-
driver/${MONGO_JAVA_DRIVER_VERSION}/mongo-java-
driver-${MONGO_JAVA_DRIVER_VERSION}.jar  
  
ARG MONGO_HADOOP_BASE_URL=https://repo1.maven.org/maven2/org/mongodb/mongo-
hadoop  
ARG MONGO_HADOOP_CORE_URL=${MONGO_HADOOP_BASE_URL}/mongo-hadoop-
core/${MONGO_HADOOP_VERSION}/mongo-hadoop-core-${MONGO_HADOOP_VERSION}.jar  
ARG MONGO_HADOOP_HIVE_URL=${MONGO_HADOOP_BASE_URL}/mongo-hadoop-
hive/${MONGO_HADOOP_VERSION}/mongo-hadoop-hive-${MONGO_HADOOP_VERSION}.jar  
ARG MONGO_HADOOP_PIG_URL=${MONGO_HADOOP_BASE_URL}/mongo-hadoop-
pig/${MONGO_HADOOP_VERSION}/mongo-hadoop-pig-${MONGO_HADOOP_VERSION}.jar  
ARG MONGO_HADOOP_SPARK_URL=${MONGO_HADOOP_BASE_URL}/mongo-hadoop-
spark/${MONGO_HADOOP_VERSION}/mongo-hadoop-spark-${MONGO_HADOOP_VERSION}.jar  
ARG MONGO_HADOOP_STREAMING_URL=${MONGO_HADOOP_BASE_URL}/mongo-hadoop-
streaming/${MONGO_HADOOP_VERSION}/mongo-hadoop-
streaming-${MONGO_HADOOP_VERSION}.jar  
  
ARG CASSANDRA_URL=http://www.apache.org/dist/cassandra  
  
ARG SPARK_CASSANDRA_BASE_URL=http://dl.bintray.com/spark-
packages/maven/datastax/spark-cassandra-connector  
ARG
SPARK_CASSANDRA_URL=${SPARK_CASSANDRA_BASE_URL}/${SPARK_CASSANDRA_VERSION}/spark-
cassandra-connector-${SPARK_CASSANDRA_VERSION}.jar  
ARG SPARK_CASSANDRA_FILE=spark-cassandra-
connector-${SPARK_CASSANDRA_VERSION}.jar  
  
ARG SPARK_HBASE_GIT=https://github.com/hortonworks-spark/shc.git  
ARG SPARK_XML_GIT=https://github.com/databricks/spark-xml.git  
ARG MONGO_REPO_URL=http://repo.mongodb.org/apt/ubuntu  
  
ARG COCKROACH_BASE_URL=https://binaries.cockroachdb.com  
ARG COCKROACH_URL=${COCKROACH_BASE_URL}/cockroach-v${COCKROACH_VERSION}.linux-
amd64.tgz  
# replaced this with the locally run script called test-versions.sh that you
should run before building the docker  
#RUN url_exists() { echo $1; if curl -s --head $1 | head -n 1 | grep
"HTTP/1.[01] [2].." ; then urlexists='YES'; else exit 1; fi } && \  
# url_exists $HADOOP_URL && \  
# url_exists $PIG_URL && \  
# url_exists $HIVE_URL && \  
# url_exists $SPARK_URL && \  
# url_exists $ZOOKEEPER_URL && \  
# url_exists $HBASE_URL && \  
# url_exists $MONGO_URL && \  
# url_exists $SPARK_CASSANDRA_URL && \  
# url_exists $MONGO_JAVA_DRIVER_URL && \  
# url_exists $MONGO_HADOOP_CORE_URL && \  
# url_exists $MONGO_HADOOP_PIG_URL && \  
# url_exists $MONGO_HADOOP_HIVE_URL && \  
# url_exists $MONGO_HADOOP_SPARK_URL && \  
# url_exists $MONGO_HADOOP_STREAMING_URL && \  
# url_exists $MONGO_JAVA_DRIVER_URL && \  
# url_exists $SPARK_CASSANDRA_URL && \  
# url_exists $COCKROACH_URL  
  
USER root  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
#ENV JAVA_HOME /usr/lib/jvm/java-1.9.0-openjdk-amd64  
ENV HADOOP_PREFIX /usr/local/hadoop  
ENV PIG_HOME /usr/local/pig  
ENV HIVE_HOME /usr/local/hive  
ENV HCAT_HOME /usr/local/hive/hcatalog  
ENV ZOOKEEPER_HOME /usr/local/zookeeper/  
ENV SPARK_HOME /usr/local/spark  
#ENV SPARK_CLASSPATH '/usr/local/spark/conf/mysql-connector-java.jar'  
ENV SPARK_CLASSPATH '/usr/local/spark/conf/mysql-connector-
java.jar:$HCAT_HOME/share/hcatalog/hcatalog-
core*.jar:$HCAT_HOME/share/hcatalog/hcatalog-pig-
adapter*.jar:$HIVE_HOME/lib/hive-
metastore-*.jar:$HIVE_HOME/lib/libthrift-*.jar:$HIVE_HOME/lib/hive-
exec-*.jar:$HIVE_HOME/lib/libfb303-*.jar:$HIVE_HOME/lib/jdo2-api-*-ec.jar:$HIVE_HOME/conf:$HADOOP_HOME/conf:$HIVE_HOME/lib/slf4j-api-*.jar'  
ENV PYTHONPATH ${SPARK_HOME}/python/:$(echo
${SPARK_HOME}/python/lib/py4j-*-src.zip):${PYTHONPATH}  
ENV HBASE_HOME /usr/local/hbase  
ENV HBASE_CONF_DIR=$HBASE_HOME/conf  
  
ENV PATH
$PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin:$PIG_HOME/bin:$HIVE_HOME/bin:$ZOOKEEPER_HOME:bin:$SPARK_HOME/bin:$HBASE_HOME/bin  
  
RUN echo "# ---------------------------------------------" && \  
echo "# passwordless ssh" && \  
echo "# ---------------------------------------------" && \  
chmod 0777 /examples && \  
apt-get update && \  
rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key /root/.ssh/id_rsa &&
\  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \  
cd /scripts && \  
echo "# ---------------------------------------------" && \  
echo "# Cockroach DB" && \  
echo "# ---------------------------------------------" && \  
mkdir /cr && \  
cd /cr && \  
wget ${COCKROACH_URL} && \  
tar xfz cockroach-* && \  
mv cockroach-v${COCKROACH_VERSION}.linux-amd64/cockroach /usr/local/bin && \  
echo "#! /bin/sh" > /scripts/start-cockroach.sh && \  
echo "cd /data" >> /scripts/start-cockroach.sh && \  
echo "cockroach start --insecure --host=localhost &" >> /scripts/start-
cockroach.sh && \  
chmod +x /scripts/start-cockroach.sh && \  
echo "#! /bin/sh" > /scripts/cockroach-shell.sh && \  
echo "cd /data" >> /scripts/cockroach-shell.sh && \  
echo "cockroach sql --insecure" >> /scripts/cockroach-shell.sh && \  
chmod +x /scripts/cockroach-shell.sh && \  
cd / && \  
rm -r /cr && \  
echo "# ---------------------------------------------" && \  
echo "# Postgresql" && \  
echo "# ---------------------------------------------" && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install postgresql postgresql-
contrib postgresql-client && \  
chmod +x /scripts/start-postgres.sh && \  
chmod +x /scripts/stop-postgres.sh && \  
chmod +x /scripts/postgres-client.sh && \  
/etc/init.d/postgresql start && \  
sudo -u postgres psql -c "create user root with password ''; alter user root
with SUPERUSER;" && \  
sudo -u postgres psql -c "create database root;" && \  
echo "# ---------------------------------------------" && \  
echo "# Make folders for HDFS data" && \  
echo "# ---------------------------------------------" && \  
mkdir /data/hdfs && \  
mkdir /data/hdfs/name && \  
mkdir /data/hdfs/data && \  
echo "# ---------------------------------------------" && \  
echo "# Hadoop" && \  
echo "# ---------------------------------------------" && \  
echo ${HADOOP_URL} && \  
curl -s ${HADOOP_URL} | tar -xz -C /usr/local/ && \  
cd /usr/local && \  
ln -s /usr/local/hadoop-${HADOOP_VERSION} /usr/local/hadoop && \  
ln -s /usr/local/hadoop-${HADOOP_VERSION} /hadoop && \  
sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr\nexport
HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh && \  
mv /usr/local/hadoop/etc/hadoop /usr/local/hadoop/etc/hadoop_backup && \  
mv /etc/my.cnf /etc/my.cnf.bak && \  
ln -s /conf/my.cnf /etc/my.cnf && \  
ln -s /conf/hadoop /usr/local/hadoop/etc/hadoop && \  
mv /conf/ssh_config /root/.ssh/config && \  
chmod 600 /root/.ssh/config && \  
chown root:root /root/.ssh/config && \  
ln -s /conf/bootstrap-mysql.sh /etc/bootstrap.sh && \  
chown root:root /etc/bootstrap.sh && \  
chmod 700 /etc/bootstrap.sh && \  
chown root:root /conf/bootstrap-mysql.sh && \  
chmod 700 /conf/bootstrap-mysql.sh && \  
chown root:root /conf/bootstrap-postgres.sh && \  
chmod 700 /conf/bootstrap-postgres.sh && \  
chmod 700 /scripts/start-hadoop.sh && \  
chmod 700 /scripts/stop-hadoop.sh && \  
ls -la /usr/local/hadoop/etc/hadoop/*-env.sh && \  
chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh && \  
ls -la /usr/local/hadoop/etc/hadoop/*-env.sh && \  
echo "# fix the 254 error code" && \  
sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config && \  
echo "UsePAM no" >> /etc/ssh/sshd_config && \  
echo "Port 2122" >> /etc/ssh/sshd_config && \  
service ssh start $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh
$HADOOP_PREFIX/sbin/start-dfs.sh $HADOOP_PREFIX/bin/hdfs dfs -mkdir -p
/user/root && \  
service ssh start $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh
$HADOOP_PREFIX/sbin/start-dfs.sh $HADOOP_PREFIX/bin/hdfs dfs -put
$HADOOP_PREFIX/etc/hadoop/ input && \  
chmod +x /scripts/loglevel-debug.sh && \  
chmod +x /scripts/loglevel-info.sh && \  
chmod +x /scripts/loglevel-warn.sh && \  
chmod +x /scripts/loglevel-error.sh && \  
echo "# ---------------------------------------------" && \  
echo "# Hive" && \  
echo ${HIVE_URL} && \  
echo "# ---------------------------------------------" && \  
curl ${HIVE_URL} | tar -zx -C /usr/local && \  
ln -s /usr/local/apache-hive-${HIVE_VERSION}-bin /usr/local/hive && \  
ln -s /usr/share/java/mysql-connector-java.jar /usr/local/hive/lib/mysql-
connector-java.jar && \  
mv /usr/local/hive/conf /usr/local/hive/conf_backup && \  
ln -s /conf/hive /usr/local/hive/conf && \  
wget https://jdbc.postgresql.org/download/postgresql-42.1.3.jar && \  
mv postgresql-42.1.3.jar /usr/local/hive/jdbc && \  
cp /usr/local/hive/jdbc/postgresql-42.1.3.jar /usr/local/hive/lib && \  
ln -s /usr/local/hive/hcatalog/share/hcatalog/hive-hcatalog-
core-${HIVE_VERSION}.jar /usr/local/hive/hcatalog/share/hcatalog/hive-
hcatalog-core.jar && \  
echo "# ---------------------------------------------" && \  
echo "# Hiveserver2 Python Package" && \  
echo "# ---------------------------------------------" && \  
apt-get -y install libsasl2-dev && \  
pip2 install PyHive && \  
pip3 install PyHive && \  
echo "# ---------------------------------------------" && \  
echo "# Pig " && \  
echo ${PIG_URL} && \  
echo "# ---------------------------------------------" && \  
curl ${PIG_URL} | tar -zx -C /usr/local && \  
ln -s /usr/local/pig-${PIG_VERSION} /usr/local/pig && \  
mv /usr/local/pig/conf /usr/local/pig/conf_backup && \  
ln -s /conf/pig /usr/local/pig/conf && \  
mkdir /usr/local/hive/hcatalog/lib && \  
ln -s /conf/hive-hcatalog-hbase-storage-handler-0.13.1.jar
/usr/local/hive/hcatalog/lib && \  
ln -s /conf/slf4j-api-1.6.0.jar /usr/local/hive/lib && \  
echo "# ---------------------------------------------" && \  
echo "# Make scripts executable" && \  
echo "# ---------------------------------------------" && \  
chmod +x /scripts/format-namenode.sh && \  
chmod +x /scripts/exit-safemode.sh && \  
chmod +x /scripts/start-thrift.sh && \  
chmod +x /scripts/init-schema-mysql.sh && \  
chmod +x /scripts/init-schema-postgres.sh && \  
chmod +x /scripts/start-everything.sh && \  
chmod +x /scripts/stop-everything.sh && \  
echo "# ---------------------------------------------" && \  
echo "# Spark" && \  
echo ${SPARK_URL} && \  
echo "# ---------------------------------------------" && \  
curl ${SPARK_URL} | tar -zx -C /usr/local && \  
ln -s /usr/local/spark-${SPARK_VERSION}-bin-hadoop2.7 /usr/local/spark && \  
ln -s /usr/local/hive/conf/hive-site.xml /usr/local/spark/conf/hive-site.xml
&& \  
ln -s /usr/share/java/mysql-connector-java.jar /usr/local/spark/conf/mysql-
connector-java.jar && \  
ln -s /usr/share/java/mysql-connector-java.jar /usr/local/spark/jars/mysql-
connector-java.jar && \  
mv /usr/local/spark/conf /usr/local/spark/conf_backup && \  
ln -s /conf/spark /usr/local/spark/conf && \  
cd /home && \  
echo "# ---------------------------------------------" && \  
echo "# HBase" && \  
echo ${HBASE_URL} && \  
echo "# ---------------------------------------------" && \  
curl ${HBASE_URL} | tar -zx -C /usr/local && \  
ln -s /usr/local/hbase-${HBASE_VERSION} /usr/local/hbase && \  
mv /usr/local/hbase/conf /usr/local/hbase/conf_backup &&\  
ln -s /conf/hbase /usr/local/hbase/conf && \  
ln -s /usr/local/hbase/bin/start-hbase.sh /scripts/starthbase.sh &&\  
ln -s /usr/local/hbase/bin/stop-hbase.sh /scripts/stophbase.sh && \  
echo "# ---------------------------------------------" && \  
echo "# Zookeeper" && \  
echo ${ZOOKEEPER_URL} && \  
echo "# ---------------------------------------------" && \  
curl ${ZOOKEEPER_URL} | tar -zx -C /usr/local && \  
ln -s /usr/local/zookeeper-${ZOOKEEPER_VERSION} /usr/local/zookeeper && \  
mkdir /usr/local/zookeeper/data && \  
mv /usr/local/zookeeper/conf /usr/local/zookeeper/conf_backup && \  
ln -s /conf/zookeeper /usr/local/zookeeper/conf && \  
pip2 install happybase psycopg2 && \  
pip3 install happybase psycopg2 && \  
echo "# ---------------------------------------------" && \  
echo "# Mongo & Cassandra Keys" && \  
echo "# ---------------------------------------------" && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb [ arch=amd64,arm64 ] ${MONGO_REPO_URL} xenial/mongodb-org/3.4
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \  
echo "deb ${CASSANDRA_URL}/debian ${CASSANDRA_VERSION}x main" | sudo tee -a
/etc/apt/sources.list.d/cassandra.sources.list && \  
curl ${CASSANDRA_URL}/KEYS | sudo apt-key add - && \  
apt-get update && \  
echo "# ---------------------------------------------" && \  
echo "# Mongo" && \  
echo "# ---------------------------------------------" && \  
apt-get -y install mongodb-org && \  
pip2 install pymongo && \  
pip3 install pymongo && \  
mkdir /data/mongo && \  
mkdir /data/mongo/data && \  
chmod +x /scripts/start-mongo.sh && \  
chmod +x /scripts/stop-mongo.sh && \  
echo "# ---------------------------------------------" && \  
echo "# Cassandra" && \  
echo ${CASSANDRA_URL} && \  
echo "# ---------------------------------------------" && \  
apt-get -y install cassandra && \  
chmod +x /scripts/start-cassandra.sh && \  
chmod +x /scripts/stop-cassandra.sh && \  
echo "# change the data and log folder" && \  
mkdir /data/cassandra && \  
mkdir /data/cassandra/data && \  
mkdir /data/cassandra/log && \  
mv /etc/cassandra /etc/cassandra_backup && \  
ln -s /conf/cassandra /etc/cassandra && \  
chmod +x /examples/cassandra/test-cassandra-table.py && \  
echo "# ---------------------------------------------" && \  
echo "# Cassandra libraries" && \  
echo "# ---------------------------------------------" && \  
pip2 install cassandra-driver && \  
pip3 install cassandra-driver && \  
echo "# ---------------------------------------------" && \  
echo "# Helper scripts" && \  
echo "# ---------------------------------------------" && \  
chmod +x /scripts/create-datadirs.sh && \  
chmod +x /scripts/delete-datadirs.sh && \  
echo "# ---------------------------------------------" && \  
cd /home && \  
echo "# Spark Cassandra Connector" && \  
echo ${SPARK_CASSANDRA_URL} && \  
echo "# ---------------------------------------------" && \  
wget ${SPARK_CASSANDRA_URL} && \  
mv /home/${SPARK_CASSANDRA_FILE} /usr/local/spark/jars && \  
ln -s /usr/local/spark/jars/${SPARK_CASSANDRA_FILE}
/usr/local/spark/jars/spark-cassandra-connector.jar && \  
echo "# ---------------------------------------------" && \  
echo "MONGO-HADOOP" && \  
echo "# ---------------------------------------------" && \  
cd /home && \  
wget \--content-disposition ${MONGO_HADOOP_CORE_URL} && \  
wget \--content-disposition ${MONGO_HADOOP_PIG_URL} && \  
wget \--content-disposition ${MONGO_HADOOP_HIVE_URL} && \  
wget \--content-disposition ${MONGO_HADOOP_SPARK_URL} && \  
wget \--content-disposition ${MONGO_HADOOP_STREAMING_URL} && \  
wget \--content-disposition ${MONGO_JAVA_DRIVER_URL} && \  
mkdir /usr/local/mongo-hadoop && \  
mv mongo-hadoop-core-${MONGO_HADOOP_VERSION}.jar /usr/local/mongo-hadoop && \  
mv mongo-hadoop-pig-${MONGO_HADOOP_VERSION}.jar /usr/local/mongo-hadoop && \  
mv mongo-hadoop-hive-${MONGO_HADOOP_VERSION}.jar /usr/local/mongo-hadoop && \  
mv mongo-hadoop-spark-${MONGO_HADOOP_VERSION}.jar /usr/local/mongo-hadoop && \  
mv mongo-hadoop-streaming-${MONGO_HADOOP_VERSION}.jar /usr/local/mongo-hadoop
&& \  
mv mongo-java-driver-${MONGO_JAVA_DRIVER_VERSION}.jar /usr/local/mongo-hadoop
&& \  
ln -s /usr/local/mongo-hadoop/mongo-hadoop-core-${MONGO_HADOOP_VERSION}.jar
/usr/local/mongo-hadoop/mongo-hadoop-core.jar && \  
ln -s /usr/local/mongo-hadoop/mongo-hadoop-pig-${MONGO_HADOOP_VERSION}.jar
/usr/local/mongo-hadoop/mongo-hadoop-pig.jar && \  
ln -s /usr/local/mongo-hadoop/mongo-hadoop-hive-${MONGO_HADOOP_VERSION}.jar
/usr/local/mongo-hadoop/mongo-hadoop-hive.jar && \  
ln -s /usr/local/mongo-hadoop/mongo-hadoop-spark-${MONGO_HADOOP_VERSION}.jar
/usr/local/mongo-hadoop/mongo-hadoop-spark.jar && \  
ln -s /usr/local/mongo-hadoop/mongo-hadoop-
streaming-${MONGO_HADOOP_VERSION}.jar /usr/local/mongo-hadoop/mongo-hadoop-
streaming.jar && \  
ln -s /usr/local/mongo-hadoop/mongo-java-
driver-${MONGO_JAVA_DRIVER_VERSION}.jar /usr/local/mongo-hadoop/mongo-java-
driver.jar && \  
cd /usr/local/mongo-hadoop && \  
git clone https://github.com/mongodb/mongo-hadoop.git && \  
cd /usr/local/mongo-hadoop/mongo-hadoop/spark/src/main/python && \  
python setup.py install && \  
python3 setup.py install && \  
echo "# ---------------------------------------------" && \  
echo "# Spark HBase" && \  
echo ${SPARK_HBASE_GIT} && \  
echo "# ---------------------------------------------" && \  
cd /tmp && \  
git clone ${SPARK_HBASE_GIT} && \  
cd /tmp/shc && \  
mvn package -DskipTests && \  
ln -s /usr/local/spark/jars/shc /usr/local/spark/jars/shc.jar && \  
cd /tmp && \  
rm -r /tmp/shc && \  
echo "# ---------------------------------------------" && \  
echo "# Spark XML library" && \  
echo "# ---------------------------------------------" && \  
cd /tmp && \  
git clone ${SPARK_XML_GIT} && \  
cd /tmp/spark-xml && \  
sbt/sbt package && \  
cp /tmp/spark-xml/target/scala-2.11/*.jar /usr/local/spark/jars && \  
ln -s /usr/local/spark/jars/spark-xml_2.11-0.4.1.jar
/usr/local/spark/jars/spark-xml.jar && \  
cd /tmp && \  
rm -r /tmp/spark-xml && \  
echo "# ---------------------------------------------" && \  
echo "# FindSpark" && \  
echo "# ---------------------------------------------" && \  
git clone https://github.com/minrk/findspark.git && \  
cd /tmp/findspark && \  
python2 setup.py install && \  
python3 setup.py install && \  
cd /home && \  
rm -r /tmp/findspark && \  
echo "# ---------------------------------------------" && \  
echo "# Miscellaneous" && \  
echo "# ---------------------------------------------" && \  
echo "alias hist='f(){ history | grep \"\$1\"; unset -f f; }; f'" >> ~/.bashrc
&& \  
echo "alias pyspark0='python -i -c\"exec(\\\\\"from initSpark import
initspark, hdfsPath\nsc, spark, conf = initspark()\nfrom pyspark.sql.types
import *\\\\\")\"'" >> ~/.bashrc && \  
echo "export PIG_OPTS=-Dhive.metastore.uris=thrift://bigdata:9083" >>
~/.bashrc && \  
echo "export PIG_CLASSPATH=$HCAT_HOME/share/hcatalog/hcatalog-
core*.jar:$HCAT_HOME/share/hcatalog/hcatalog-pig-
adapter*.jar:$HIVE_HOME/lib/hive-
metastore-*.jar:$HIVE_HOME/lib/libthrift-*.jar:$HIVE_HOME/lib/hive-
exec-*.jar:$HIVE_HOME/lib/libfb303-*.jar:$HIVE_HOME/lib/jdo2-api-*-ec.jar:$HIVE_HOME/conf:$HADOOP_HOME/conf:$HIVE_HOME/lib/slf4j-api-*.jar"
>> ~/.bashrc && \  
echo "export HCAT_HOME=/usr/local/hive/hcatalog" >> ~/.bashrc && \  
echo "# Final Cleanup" && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
echo "*************"  
  
RUN echo "*************" && \  
echo "" >> /scripts/notes.txt  
  
CMD ["/etc/bootstrap.sh", "-d"]  
# end of actual build  
# export SPARK_XML_GIT=https://github.com/databricks/spark-xml.git  
# echo "# ---------------------------------------------" && \  
# echo "# Spark HBase" && \  
# echo ${SPARK_HBASE_GIT} && \  
# echo "# ---------------------------------------------" && \  
# cd /tmp  
# git clone ${SPARK_HBASE_GIT} && \  
# cd /tmp/shc && \  
# mvn package -DskipTests && \  
# mvn clean package test && \  
# mvn -DwildcardSuites=org.apache.spark.sql.DefaultSourceSuite test && \  
# cp /tmp/shc/target/scala-2.11/*.jar /usr/local/spark/jars && \  
# ln -s /usr/local/spark/jars/shc /usr/local/spark/jars/shc.jar && \  
# cd /tmp && \  
# rm -r /rmp/shc  
# echo "# ---------------------------------------------" && \  
# echo "# Spark XML library" && \  
# echo "# ---------------------------------------------" && \  
# cd /home && \  
# git clone ${SPARK_XML_GIT} && \  
# cd /home/spark-xml && \  
# sbt/sbt package && \  
# cp /home/spark-xml/target/scala-2.11/*.jar /usr/local/spark/jars && \  
# ln -s /usr/local/spark/jars/spark-xml_2.11-0.4.1.jar
/usr/local/spark/jars/spark-xml.jar && \  
# cd /home && \  
# rm -r /home/spark-xml && \  
# cd /home && \  
# git clone https://github.com/minrk/findspark.git && \  
# cd /home/findspark && \  
# python2 setup.py install && \  
# python3 setup.py install && \  
# cd /home && \  
# rm -r /home/findspark && \  
# echo "# ---------------------------------------------" && \  
# echo "# Cockroach DB" && \  
# echo "# ---------------------------------------------" && \  
# wget ${COCKROACH_URL} && \  
# tar xfz cockroach-* && \  
# mv cockroach-v${COCKROACH_VERSION}.linux-amd64/cockroach /usr/local/bin && \  
# rm -r /scripts/cockroach* && \  
# echo "#! /bin/sh" > /scripts/start-cockroach.sh && \  
# echo "cd /data" >> /scripts/start-cockroach.sh && \  
# echo "cockroach start --insecure --host=localhost &" >> /scripts/start-
cockroach.sh && \  
# chmod +x /scripts/start-cockroach.sh && \  
# echo "#! /bin/sh" > /scripts/cockroach-shell.sh && \  
# echo "cd /data" >> /scripts/cockroach-shell.sh && \  
# echo "cockroach sql --insecure" >> /scripts/cockroach-shell.sh && \  
# chmod +x /scripts/cockroach-shell.sh && \  
# hive --service hiveserver2 start  
# hive --service hiveserver2 stop  
# sudo service hive-server2 start  
# !connect jdbc:hive2://localhost:10000  
#<name>hadoop.proxyuser.hive.groups</name>  
#<value>*</value>  
#</property>  
#<property>  
#<name>hadoop.proxyuser.hive.hosts</name>  
#<value>*</value>  
#</property>  
# <property>  
# <name>hive.server2.enable.doAs</name>  
# <value>false</value>  
# </property>  
#https://repo1.maven.org/maven2/org/apache/parquet/parquet-pig/1.9.0/parquet-
pig-1.9.0.jar  
#https://repo1.maven.org/maven2/com/twitter/elephantbird/elephant-bird-
pig/4.9/elephant-bird-pig-4.9.jar  
# hive on spark  
#ln -s /usr/local/spark/jars/scala-library-*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/spark-core_*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/spark-network-common_*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/chill-java*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/chill*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/jackson-module-paranamer*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/jackson-module-scala*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/jersey-container-servlet-core*.jar
/usr/local/hive/lib  
#ln -s /usr/local/spark/jars/jersey-server*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/json4s-ast*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/kryo-shaded*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/minlog*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/scala-xml*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/spark-launcher*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/spark-network-shuffle*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/spark-unsafe*.jar /usr/local/hive/lib  
#ln -s /usr/local/spark/jars/xbean-asm5-shaded*.jar /usr/local/hive/lib  
#mkdir /tmp/spark  
#set hive.execution.engine=spark;  
#use northwind;  
#select c.categoryid, c.categoryname, p.productid, p.productname from
categories as c join products as p on c.categoryid = p.categoryid;  
# export HCAT_HOME=/usr/local/hive/hcatalog  
# alias and export pig  
# start-hbase.sh  
# make scripts executable removed  
# chmod +x /scripts/start-hiveserver.sh && \  

