FROM ubuntu:16.04  
  
# Install Python ( to support pyspark )  
# This must be done before installing mesos to prevent conflicts later  
# "new installation of python2.7-minimal; /usr/lib/python2.7/site-packages is
a directory"  
# "which is expected a symlink to /usr/local/lib/python2.7/dist-packages."  
RUN \  
apt-get update && \  
apt-get install -y python && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Mesos ( and jdk )  
# Pinned version in use here  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv E56151BF && \  
echo "deb http://repos.mesosphere.com/ubuntu xenial main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get update && \  
apt-get install -y \  
default-jdk \  
mesos=1.1.0-2.0.107.ubuntu1604 && \  
rm -fr /var/lib/apt/list/*  
  
# Install Spark  
# Pinned version in use here  
RUN \  
apt-get update && \  
apt-get install -y curl && \  
curl http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz | tar
-xzC /opt && \  
mv /opt/spark-* /opt/spark && \  
apt-get autoremove -y curl && \  
rm -fr /var/lib/apt/list/*  
  
ENV \  
JAVA_HOME=/usr/lib/jvm/default-java \  
SPARK_HOME=/opt/spark  
  
ENV \  
PATH=${SPARK_HOME}/bin:${JAVA_HOME}/bin:${PATH}  

