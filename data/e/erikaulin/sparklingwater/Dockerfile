FROM ubuntu:14.04  
  
MAINTAINER Erik Aulin <erik@aulin.co>  
  
# add a post-invoke hook to dpkg which deletes cached deb files  
# update the sources.list  
# update/dist-upgrade  
RUN \  
echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
echo "deb http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu trusty main
universe" >> /etc/apt/sources.list && \  
apt-get update -q -y && \  
apt-get dist-upgrade -y  
  
# Install Oracle Java 7  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget unzip software-
properties-common python-software-properties && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update -q && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java7-installer && \  
apt-get clean  
  
# Install additional tools  
RUN apt-get -y install --no-install-recommends \  
less \  
curl \  
vim-tiny \  
sudo \  
openssh-server \  
unzip  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/apt/*  
  
# Install Spark 1.6.1  
RUN curl -s https://archive.apache.org/dist/spark/spark-1.6.1/spark-1.6.1-bin-
cdh4.tgz | tar -xz -C /opt && \  
ln -s /opt/spark-1.6.1-bin-cdh4 /opt/spark && \  
mkdir /opt/spark/work && \  
chmod 0777 /opt/spark/work  
  
# Install Sparkling water latest version  
RUN curl -s http://h2o-release.s3.amazonaws.com/sparkling-
water/rel-1.6/3/sparkling-water-1.6.3.zip --output sw.zip && \  
unzip sw.zip -d /opt/ && \  
ln -s /opt/sparkling-water-1.6.3 /opt/sparkling-water && \  
rm -f sw.zip  
  
ADD scripts/start-master.sh /start-master.sh  
ADD scripts/start-worker /start-worker.sh  
ADD scripts/spark-shell.sh /spark-shell.sh  
ADD scripts/spark-defaults.conf /spark-defaults.conf  
ADD scripts/remove_alias.sh /remove_alias.sh  
  
ENV SPARK_HOME /opt/spark  
ENV SPARKLING_WATER_HOME /opt/sparkling-water  
  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_WORKER_PORT 8888  
ENV SPARK_WORKER_WEBUI_PORT 8081  
  
EXPOSE 8080 7077 8888 8081 4040 7001 7002 7003 7004 7005 7006 54321  

