# Copyright KOLIBERO under one or more contributor license agreements.  
# KOLIBERO licenses this file to You under the Apache License, Version 2.0  
# (the "License"); you may not use this file except in compliance with  
# the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM ubuntu:14.04  
MAINTAINER Piotr Goliasz <piotr.goliasz@kolibero.eu>  
  
ENV PIO_VERSION 0.10.0  
ENV SPARK_VERSION 1.6.1  
ENV ELASTICSEARCH_VERSION 1.4.4  
ENV HBASE_VERSION 1.0.0  
ENV PIO_HOME /PredictionIO-${PIO_VERSION}  
ENV PATH=${PIO_HOME}/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get -y update  
RUN apt-get -y -q install software-properties-common  
RUN add-apt-repository ppa:openjdk-r/ppa  
  
RUN apt-get update \  
&& apt-get install -y curl openjdk-8-jdk libgfortran3 python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -O
http://mirror.nexcess.net/apache/incubator/predictionio/${PIO_VERSION}-incubating/apache-
predictionio-${PIO_VERSION}-incubating.tar.gz \  
&& tar -xvzf apache-predictionio-${PIO_VERSION}-incubating.tar.gz -C / \  
&& rm apache-predictionio-${PIO_VERSION}-incubating.tar.gz \  
&& cd apache-predictionio-${PIO_VERSION}-incubating \  
&& ./make-distribution.sh  
  
RUN tar zxvf /apache-
predictionio-${PIO_VERSION}-incubating/PredictionIO-${PIO_VERSION}-incubating.tar.gz
-C /  
RUN rm -r /apache-predictionio-${PIO_VERSION}-incubating  
RUN mv ${PIO_HOME}-incubating ${PIO_HOME}  
RUN mkdir -p ${PIO_HOME}/vendors  
COPY files/pio-env.sh ${PIO_HOME}/conf/pio-env.sh  
  
RUN curl -O http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-
hadoop2.6.tgz \  
&& tar -xvzf spark-${SPARK_VERSION}-bin-hadoop2.6.tgz -C ${PIO_HOME}/vendors \  
&& rm spark-${SPARK_VERSION}-bin-hadoop2.6.tgz  
  
RUN curl -O
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz
\  
&& tar -xvzf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz -C
${PIO_HOME}/vendors \  
&& rm elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \  
&& echo 'cluster.name: predictionio' >>
${PIO_HOME}/vendors/elasticsearch-${ELASTICSEARCH_VERSION}/config/elasticsearch.yml
\  
&& echo 'network.host: 127.0.0.1' >>
${PIO_HOME}/vendors/elasticsearch-${ELASTICSEARCH_VERSION}/config/elasticsearch.yml  
  
RUN curl -O
http://archive.apache.org/dist/hbase/hbase-${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz
\  
&& tar -xvzf hbase-${HBASE_VERSION}-bin.tar.gz -C ${PIO_HOME}/vendors \  
&& rm hbase-${HBASE_VERSION}-bin.tar.gz  
COPY files/hbase-site.xml
${PIO_HOME}/vendors/hbase-${HBASE_VERSION}/conf/hbase-site.xml  
RUN sed -i "s|VAR_PIO_HOME|${PIO_HOME}|"
${PIO_HOME}/vendors/hbase-${HBASE_VERSION}/conf/hbase-site.xml \  
&& sed -i "s|VAR_HBASE_VERSION|${HBASE_VERSION}|"
${PIO_HOME}/vendors/hbase-${HBASE_VERSION}/conf/hbase-site.xml  
  
#triggers fetching the complete sbt environment  
RUN ${PIO_HOME}/sbt/sbt -batch  

