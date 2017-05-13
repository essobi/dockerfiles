# Copyright (c) Mihai Paraschiv.
# Distributed under the terms of the Modified BSD License.

FROM mihaiparaschiv/data-science-base:0.2.0
MAINTAINER Mihai Paraschiv <mihai.paraschiv@gmail.com>


USER root

# Install Spark
ENV APACHE_SPARK_VERSION 2.0.0
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends openjdk-7-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN cd /tmp && \
        wget -q http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz && \
        echo "8a14410a906926d2593e45e1ffd7e26c4e9223df94ad9902fc62cad6b900a8fcc22944fb6e9dfc2c4b35066a7d0c1e676ce4d0db35dee36dac2deea6b83c1f24 *spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz" | shasum -a 512 -c - && \
        tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz -C /usr/local && \
        rm spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7.tgz
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop2.7 spark

# Spark configuration
ENV SPARK_HOME /usr/local/spark
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.1-src.zip
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info
ENV R_LIBS_USER $SPARK_HOME/R/lib

USER $NB_USER