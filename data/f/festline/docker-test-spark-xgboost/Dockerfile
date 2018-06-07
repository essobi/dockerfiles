# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/scipy-notebook  
  
MAINTAINER Yury Kashnitsky  
  
USER root  
  
# Spark dependencies  
ENV APACHE_SPARK_VERSION 1.6.1  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends openjdk-7-jre-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN cd /tmp && \  
wget -q
http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-
hadoop2.6.tgz && \  
echo "09f3b50676abc9b3d1895773d18976953ee76945afa72fa57e6473ce4e215970
*spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz" | sha256sum -c - && \  
tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz -C /usr/local && \  
rm spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6.tgz  
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.6 spark  
  
# Spark config  
ENV SPARK_HOME /usr/local/spark  
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.9-src.zip  
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
--driver-java-options=-Dlog4j.logLevel=info  
  
  
# Install XGBoost library  
RUN git clone \--recursive https://github.com/dmlc/xgboost && \  
cd xgboost && \  
make -j4 && \  
cd python-package; python setup.py install && cd ../..  
  
# update main conda packages  
RUN conda install --quiet --yes numpy scipy pandas matplotlib seaborn scikit-
learn  
  
USER $NB_USER

