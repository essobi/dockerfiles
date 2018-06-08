# -------------------------------------  
# Based on debian:jessie => 123MB  
# -------------------------------------  
FROM debian:jessie  
  
  
# -------------------------------------  
# INFO => 123MB  
# -------------------------------------  
# environmentType like development/staging/production  
ARG environmentType=development  
  
MAINTAINER "Alberto Falchi"  
LABEL project="maestro-distributed-platform"  
LABEL version = "0.0.0"  
LABEL author="Alberto Falchi"  
LABEL author_email="alberto.falchi@ohiaia.com"  
LABEL author_nickname="ohiaia"  
LABEL environmentType="${environmentType}"  
  
# -------------------------------------  
# Tools Packages => 171MB  
# -------------------------------------  
RUN apt-get update \  
&& apt-get install -y locales \  
&& dpkg-reconfigure -f noninteractive locales \  
&& locale-gen C.UTF-8 \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Users with other locales should set this in their derivative image  
# ARG PYTHON_VERSION=3  
ARG LANG=en_US.UTF-8  
ARG LANGUAGE=en_US:en  
ARG LC_ALL=en_US.UTF-8  
RUN apt-get update \  
&& apt-get install -y curl unzip  
  
# -------------------------------------  
# Java => 321MB  
# -------------------------------------  
ARG JAVA_MAJOR_VERSION=8  
ARG JAVA_UPDATE_VERSION=131  
ARG JAVA_BUILD_NUMBER=11  
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
ENV PATH $PATH:$JAVA_HOME/bin  
  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/d54c1d3a095b4ff2b6607d096fa80163/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
# -------------------------------------  
# HADOOP => 569MB  
# -------------------------------------  
ARG HADOOP_VERSION=2.7.3  
ENV HADOOP_HOME /usr/hadoop-${HADOOP_VERSION}  
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop  
ENV PATH $PATH:${HADOOP_HOME}/bin  
  
RUN curl -sL --retry 3 \  
"http://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"
\  
| gunzip \  
| tar -x -C /usr/ \  
&& rm -rf ${HADOOP_HOME}/share/doc \  
&& chown -R root:root ${HADOOP_HOME}  
  
# -------------------------------------  
# SPARK => 721MB  
# -------------------------------------  
ARG SPARK_HOME=/opt/spark  
ARG SPARK_VERSION=2.2.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop  
ENV
SPARK_DIST_CLASSPATH="${HADOOP_HOME}/etc/hadoop/*:${HADOOP_HOME}/share/hadoop/common/lib/*:${HADOOP_HOME}/share/hadoop/common/*:${HADOOP_HOME}/share/hadoop/hdfs/*:${HADOOP_HOME}/share/hadoop/hdfs/lib/*:${HADOOP_HOME}/share/hadoop/hdfs/*:${HADOOP_HOME}/share/hadoop/yarn/lib/*:${HADOOP_HOME}/share/hadoop/yarn/*:${HADOOP_HOME}/share/hadoop/mapreduce/lib/*:${HADOOP_HOME}/share/hadoop/mapreduce/*:${HADOOP_HOME}/share/hadoop/tools/lib/*"  
ENV PATH $PATH:${SPARK_HOME}/bin  
  
RUN curl -sL --retry 3 \  
"http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \  
| gunzip \  
| tar x -C /usr/ \  
&& mv /usr/$SPARK_PACKAGE $SPARK_HOME \  
&& chown -R root:root $SPARK_HOME  
  
# -------------------------------------  
# Python => 761MB  
# -------------------------------------  
# python's  
ARG PYTHON_VERSION=3  
# pre-clean  
RUN apt-get purge -y python  
RUN apt-get autoclean && apt-get -y autoremove  
  
RUN apt-get install -y \  
python${PYTHON_VERSION} \  
python${PYTHON_VERSION}-setuptools  
  
RUN ln -s /usr/bin/python3 /usr/bin/python  
  
RUN easy_install3 pip py4j  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Some Little Python compatibility fix  
# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-
pythonhashseed  
ENV PYTHONHASHSEED 0  
ENV PYTHONIOENCODING UTF-8  
ENV PIP_DISABLE_PIP_VERSION_CHECK 1  
# -------------------------------------  
# PySpark => 1.17 GB  
# -------------------------------------  
RUN pip install pyspark  
  
# -------------------------------------  
# Servo starts =>  
# -------------------------------------  
# Add sweet starters for simplified k8s-dockerized uses  
ADD ./stack /servos  
WORKDIR /servos/start  
RUN chmod +x *.sh  
  
# Back to root  
WORKDIR /  

