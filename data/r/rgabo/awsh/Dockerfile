FROM python:3.5  
MAINTAINER Gabor Ratky <rgabo@rgabostyle.com>  
  
# Spark dependencies  
ENV APACHE_SPARK_VERSION 2.0.0  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends openjdk-7-jre-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV HADOOP_VERSION 2.7  
RUN cd /tmp && \  
wget -q
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz && \  
echo "3d46e990c06a362efc23683cf0ec15e1943c28e023e5b5d4e867c78591c937ad
*spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha256sum -c
- && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C
/usr/local && \  
rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION} spark  
  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $PATH:$SPARK_HOME/bin  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.1-src.zip  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
  
# awscli & s3cmd  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends awscli s3cmd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# fuse & syslog-ng  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends fuse syslog-ng && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ADD etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
  
# goofys (S3)  
RUN cd /usr/bin && \  
wget -q https://github.com/kahing/goofys/releases/download/v0.0.8/goofys && \  
chmod +x goofys  
  
# workspaces  
RUN mkdir -p /buckets  
  
# local workspace  
RUN mkdir -p /local  
WORKDIR /local  
  
# awsh  
RUN mkdir -p /awsh  
  
COPY requirements.txt /awsh/requirements.txt  
RUN pip install -r /awsh/requirements.txt  
  
COPY requirements-test.txt /awsh/requirements-test.txt  
RUN pip install -r /awsh/requirements-test.txt  
  
COPY . /awsh  
RUN pip install /awsh  
  
# entrypoint  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

