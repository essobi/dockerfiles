FROM jupyter/minimal-notebook  
  
MAINTAINER Khwunchai Jaengsawang <khwunchai.j@ku.th>  
  
USER root  
  
# Spark dependencies  
ENV APACHE_SPARK_VERSION 2.2.0  
ENV HADOOP_VERSION 2.7  
# Temporarily add jessie backports to get openjdk 8, but then remove that
source  
RUN echo 'deb http://cdn-fastly.deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get -y update && \  
apt-get install --no-install-recommends -t jessie-backports -y openjdk-8-jre-
headless ca-certificates-java && \  
rm /etc/apt/sources.list.d/jessie-backports.list && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Apache Spark  
RUN cd /tmp && \  
wget -q
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${  
}.tgz && \  
echo
"3fc94096ae34f9a1a148d37e5ed640a7e5de1812f1f2ecd715d92bbf2901e895cf4b93e6d8ee0d64debb5df7c56d673c0a36e5fc49503ec0f4507eb0edf961a4
*spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c
- && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C
/usr/local && \  
rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION} spark  
  
# Spark config  
ENV SPARK_HOME /usr/local/spark  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_USER  
  
# Apache Toree kernel  
RUN pip --no-cache-dir install
https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0/snapshots/dev1/toree-
pip/toree-0.2.0.dev1.tar.gz  
RUN jupyter toree install --sys-prefix  

