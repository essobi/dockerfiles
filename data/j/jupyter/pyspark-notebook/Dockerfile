# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/scipy-notebook  
  
LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"  
  
USER root  
  
# Spark dependencies  
ENV APACHE_SPARK_VERSION 2.3.0  
ENV HADOOP_VERSION 2.7  
RUN apt-get -y update && \  
apt-get install --no-install-recommends -y openjdk-8-jre-headless ca-
certificates-java && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp && \  
wget -q
http://apache.claz.org/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz && \  
echo
"258683885383480BA01485D6C6F7DC7CFD559C1584D6CEB7A3BBCF484287F7F57272278568F16227BE46B4F92591768BA3D164420D87014A136BF66280508B46
*spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c
- && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C
/usr/local \--owner root --group root --no-same-owner && \  
rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION} spark  
  
# Mesos dependencies  
# Install from the Xenial Mesosphere repository since there does not (yet)  
# exist a Bionic repository and the dependencies seem to be compatible for
now.  
COPY mesos.key /tmp/  
RUN apt-get -y update && \  
apt-get install --no-install-recommends -y gnupg && \  
apt-key add /tmp/mesos.key && \  
echo "deb http://repos.mesosphere.io/ubuntu xenial main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get -y update && \  
apt-get --no-install-recommends -y install mesos=1.2\\* && \  
apt-get purge --auto-remove -y gnupg && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Spark and Mesos config  
ENV SPARK_HOME /usr/local/spark  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.6-src.zip  
ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
  
USER $NB_UID  
  
# Install pyarrow  
RUN conda install --quiet -y 'pyarrow' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  

