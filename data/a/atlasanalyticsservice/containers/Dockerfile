FROM centos:7  
LABEL maintainer="Ilija Vukotic <ivukotic@cern.ch>"  
  
RUN yum install -y epel-release.noarch  
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum -y update  
  
# Install dependencies  
RUN yum install -y \  
httpd \  
git \  
curl \  
wget \  
rsync \  
zip \  
unzip \  
vim \  
libaio \  
python-pip \  
python-devel \  
python36u \  
python36u-pip \  
python36u-devel \  
ntp \  
krb5-workstation \  
mod_auth_kerb \  
mod_ssl \  
mod_wsgi \  
openssl-devel \  
java-1.7.0-openjdk-devel \  
java-1.8.0-openjdk-devel  
  
# mysql-connector-java  
# build-essential \  
# krb5-user \  
# libzmq3-dev \  
# pkg-config \  
# software-properties-common \  
# zlib1g-dev  
# module-init-tools \  
# openjdk-8-jdk \  
# openjdk-8-jre-headless \  
# pig  
#RUN curl -LO
https://download.java.net/openjdk/jdk9/ri/openjdk-9+181_linux-x64_ri.zip  
#RUN unzip openjdk-9+181_linux-x64_ri.zip  
ENV JAVA_HOME /etc/alternatives/java_sdk_1.7.0_openjdk/jre/  
  
# ENV PIG_VERSION 0.17.0  
# RUN curl -LO
http://apache.cs.utah.edu/pig/pig-$PIG_VERSION/pig-$PIG_VERSION.tar.gz  
# RUN tar xzf pig-$PIG_VERSION.tar.gz  
# RUN rm pig-$PIG_VERSION.tar.gz  
# ENV PATH $PATH:/pig-$PIG_VERSION/bin  
# # es-hadoop - for all the modules (pig, mr, spark)  
ENV EH_VERSION 6.2.2  
RUN curl -LO https://artifacts.elastic.co/downloads/elasticsearch-
hadoop/elasticsearch-hadoop-$EH_VERSION.zip  
RUN unzip elasticsearch-hadoop-$EH_VERSION.zip  
RUN mkdir /elasticsearch-hadoop && \  
ln -s /elasticsearch-hadoop-$EH_VERSION/dist/elasticsearch-
hadoop-$EH_VERSION.jar /elasticsearch-hadoop/elasticsearch-hadoop.jar && \  
ln -s /elasticsearch-hadoop-$EH_VERSION/dist/elasticsearch-hadoop-
pig-$EH_VERSION.jar /elasticsearch-hadoop/elasticsearch-hadoop-pig.jar && \  
ln -s /elasticsearch-hadoop-$EH_VERSION/dist/elasticsearch-
spark-20_2.11-$EH_VERSION.jar /elasticsearch-hadoop/elasticsearch-spark.jar  
  
# hdfs  
RUN wget http://archive.cloudera.com/cdh5/one-click-
install/redhat/7/x86_64/cloudera-cdh-5-0.x86_64.rpm  
RUN yum install -y localinstall cloudera-cdh-5-0.x86_64.rpm  
RUN yum install -y pig \  
hbase \  
flume-ng  
  
# elephant-bird  
ENV EB_VERSION 4.17  
RUN wget http://central.maven.org/maven2/com/twitter/elephantbird/elephant-
bird-hadoop-compat/$EB_VERSION/elephant-bird-hadoop-compat-$EB_VERSION.jar -O
/usr/lib/pig/lib/elephant-bird-hadoop-compat.jar  
RUN wget http://central.maven.org/maven2/com/twitter/elephantbird/elephant-
bird-core/$EB_VERSION/elephant-bird-core-$EB_VERSION.jar -O
/usr/lib/pig/lib/elephant-bird-core.jar  
RUN wget http://central.maven.org/maven2/com/twitter/elephantbird/elephant-
bird-pig/$EB_VERSION/elephant-bird-pig-$EB_VERSION.jar -O
/usr/lib/pig/lib/elephant-bird-pig.jar  
  
# sqoop1  
RUN wget
http://mirrors.sonic.net/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz  
RUN mkdir -p /usr/local/sqoop  
RUN tar -xvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz --directory /usr/local/sqoop
--strip-components=1  
  
# mysql  
RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.45.tar.gz  
RUN mkdir -p /usr/local/mysql  
RUN tar -xvf mysql-connector-java-5.1.45.tar.gz --directory /usr/local/mysql
--strip-components=1  
RUN cp /usr/local/mysql/mysql-connector-java-5.1.45-bin.jar /usr/local/sqoop  
  
ENV HADOOP_MAPRED_HOME /usr/lib/hadoop-mapreduce  
ENV HADOOP_COMMON_HOME /usr/lib/hadoop  
  
RUN rm sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz \  
elasticsearch-hadoop-$EH_VERSION.zip \  
mysql-connector-java-5.1.45.tar.gz  
  
COPY configs/core-site.xml configs/hdfs-site.xml configs/mapred-site.xml
configs/yarn-site.xml /etc/hadoop/conf/  
  
COPY Unconfirmed.zip /usr/local/sqoop/lib/ojdbc6.jar  
RUN chmod 755 /usr/local/sqoop/lib/ojdbc6.jar  
  
RUN pip install --upgrade pip  
RUN pip install --no-cache-dir \  
h5py \  
tables \  
numpy \  
pandas \  
scipy \  
sklearn \  
elasticsearch \  
cx_Oracle \  
requests \  
stomp.py  
  
# python3  
RUN pip3.6 install --upgrade pip  
RUN pip3.6 install --no-cache-dir \  
h5py \  
tables \  
numpy \  
pandas \  
scipy \  
sklearn \  
elasticsearch \  
cx_Oracle \  
requests \  
stomp.py  
  
COPY configs/krb5.conf /etc/krb5.conf  
  
COPY run.sh run.sh  
RUN chmod 755 run.sh  
  
COPY xAOD/run.sh xAOD/  
RUN chmod 755 xAOD/run.sh  
  
COPY FTS/run.sh FTS/  
RUN chmod 755 FTS/run.sh  
  
COPY DistributedProcessing/run.sh DistributedProcessing/  
RUN chmod 755 DistributedProcessing/run.sh  
  
COPY BOINC/run.sh BOINC/  
RUN chmod 755 BOINC/run.sh  
COPY BOINC/run-dev.sh BOINC/  
RUN chmod 755 BOINC/run-dev.sh  
COPY BOINC/run-cms-dev.sh BOINC/  
RUN chmod 755 BOINC/run-cms-dev.sh  
  
COPY DDM/run.sh DDM/  
RUN chmod 755 DDM/run.sh  
  
# build info  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt  
  
RUN useradd -ms /bin/bash analyticssvc  
  
USER analyticssvc  
WORKDIR /home/analyticssvc  
  
#execute service  
CMD ["/run.sh"]  

