# changed by adolphlwq, refer to https://github.com/jupyter/docker-stacks  
# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM adolphlwq/docker-jupyter:base-notebook-23  
MAINTAINER adolphlwq kenan3015@gmail.com  
  
USER root  
# Spark dependencies  
ENV APACHE_SPARK_VERSION=2.0.1 \  
MESOS_VERSION=0.28.1 \  
SPARK_URL=http://archive.apache.org/dist/spark/spark-2.0.2/spark-2.0.2-bin-
hadoop2.7.tgz  
ENV SPARK_CASSANDRA_COLLECTOR http://dl.bintray.com/spark-
packages/maven/datastax/spark-cassandra-connector/2.0.0-M2-s_2.11/spark-
cassandra-connector-2.0.0-M2-s_2.11.jar  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends openjdk-7-jre-headless curl wget &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# download Spark 2.0.2  
RUN curl -fL $SPARK_URL | tar xzf - -C /usr/local  
  
#download Mesos 0.28.1  
RUN echo "deb http://repos.mesosphere.io/ubuntu/ trusty main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
apt-get -y update && \  
apt-get --no-install-recommends -y --force-yes install
mesos=0.28.1-2.0.20.ubuntu1404 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# install cassandra-driver  
RUN pip3 install cassandra-driver matplotlib pandas numpy scipy scikit-learn
&& \  
pip2 install cassandra-driver matplotlib pandas numpy scipy scikit-learn  
  
# Spark and Mesos config  
ENV SPARK_HOME /usr/local/spark-2.0.2-bin-hadoop2.7  
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.3-src.zip \  
MESOS_NATIVE_JAVA_LIBRARY=/usr/local/lib/libmesos.so  
#ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-
options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info  
# add spark cassandra collector  
RUN wget $SPARK_CASSANDRA_COLLECTOR -O $SPARK_HOME/jars/spark-cassandra-
connector-2.0.0-M2-s_2.11.jar  
USER $NB_USER  

