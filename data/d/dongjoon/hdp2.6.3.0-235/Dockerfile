# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM dongjoon/ubuntu16.04-jdk8  
MAINTAINER Dongjoon Hyun <dongjoon@apache.org>  
  
# HDP 2.6.3  
RUN \  
wget http://public-
repo-1.hortonworks.com/HDP/ubuntu16/2.x/updates/2.6.3.0/hdp.list -O
/etc/apt/sources.list.d/hdp.list && \  
apt-get update && \  
apt-get clean  
  
RUN apt-get install -y --allow-unauthenticated hadoop-2-6-3* hive-2-6-3*
hive2-2-6-3* spark-2-6-3* spark2-2-6-3* vim git  
  
ENV HADOOP_PREFIX /usr/hdp/2.6.3.0-235/hadoop  
  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
RUN \  
echo 'HADOOP_PREFIX="/usr/hdp/2.6.3.0-235/hadoop"' >> /etc/environment && \  
echo 'HADOOP_COMMON_HOME="/usr/hdp/2.6.3.0-235/hadoop"' >> /etc/environment &&
\  
echo 'HADOOP_HDFS_HOME="/usr/hdp/2.6.3.0-235/hadoop"' >> /etc/environment && \  
echo 'HADOOP_MAPRED_HOME="/usr/hdp/2.6.3.0-235/hadoop"' >> /etc/environment &&
\  
echo 'HADOOP_YARN_HOME="/usr/hdp/2.6.3.0-235/hadoop-yarn"' >> /etc/environment
&& \  
echo 'HADOOP_CONF_DIR="/usr/hdp/2.6.3.0-235/hadoop/etc/hadoop"' >>
/etc/environment && \  
echo 'YARN_CONF_DIR="/usr/hdp/2.6.3.0-235/hadoop/etc/hadoop"' >>
/etc/environment  
ENV PATH $PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin:$HADOOP_PREFIX-
yarn/bin:$HADOOP_PREFIX-yarn/sbin:$HADOOP_PREFIX-hdfs/bin:$HADOOP_PREFIX-
hdfs/sbin  
  
COPY core-site.xml $HADOOP_PREFIX/etc/hadoop/  
COPY hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/  
COPY mapred-site.xml $HADOOP_PREFIX/etc/hadoop/  
COPY yarn-site.xml $HADOOP_PREFIX/etc/hadoop/  
RUN sed -i.bak
'/<configuration>/a\\\n<property>\n<name>hive.metastore.schema.verification</name>\n<value>false</value>\n</property>\n'
/etc/hive/conf/hive-site.xml  
RUN cp /etc/hive/conf/hive-site.xml /etc/spark/conf/  
RUN cp /etc/hive/conf/hive-site.xml /etc/spark2/conf/  
  
COPY init-nn.sh /root/  
  
EXPOSE 22 4040 7077 8020 8030 8031 8032 8033 8040 8042 8080 8088 10000 50010
50020 50060 50070 50075 50090  

