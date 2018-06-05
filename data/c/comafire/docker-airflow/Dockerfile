FROM ubuntu:16.04  
MAINTAINER comafire <comafire@gmail.com>  
  
# Bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Common  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential vim curl wget git cmake bzip2 sudo locales unzip net-tools \  
libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev
llvm \  
libfreetype6-dev libxft-dev  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common libjpeg-dev libpng-dev ncurses-dev imagemagick \  
libgraphicsmagick1-dev libzmq-dev gfortran gnuplot gnuplot-x11 libsdl2-dev \  
apt-utils openssh-client  
  
# Docker  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https ca-certificates  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
-  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
RUN apt-get update && apt-get install -y --no-install-recommends \  
docker-ce  
  
# Database  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libmysqlclient-dev libpq-dev  
  
# Python2  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python python-dev python-pip python-virtualenv python-software-properties  
RUN pip2 install --upgrade pip  
RUN pip2 install setuptools  
  
# Python2-Deps  
RUN pip2 install matplotlib pandas pandas-datareader quandl  
RUN pip2 install numpy scipy sklearn tensorflow  
RUN pip2 install docker fabric pytest pycrypto  
RUN pip2 install pymysql airflow airflow[mysql,crypto,password]  
  
# Python3  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python3 python3-dev python3-pip python3-virtualenv python3-software-properties  
RUN pip3 install --upgrade pip  
RUN pip3 install setuptools  
  
# Python3-Deps  
RUN pip3 install matplotlib pandas pandas-datareader quandl  
RUN pip3 install numpy scipy sklearn tensorflow  
RUN pip3 install docker fabric pytest pycrypto  
RUN pip3 install pymysql airflow airflow[mysql,crypto,password]  
  
# JAVA  
ARG JAVA_MAJOR_VERSION=8  
ARG JAVA_UPDATE_VERSION=131  
ARG JAVA_BUILD_NUMBER=11  
ARG ORACLE_TOKEN=d54c1d3a095b4ff2b6607d096fa80163  
ENV JAVA_HOME /usr/local/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/${ORACLE_TOKEN}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/local/ \  
&& ln -s $JAVA_HOME /usr/local/java \  
&& rm -rf $JAVA_HOME/man  
  
# Scala  
RUN apt-get update && apt-get install -y --no-install-recommends \  
scala  
RUN pip2 install py4j  
RUN pip3 install py4j  
  
# SPARK  
ENV SPARK_VERSION 2.1.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-hadoop2.7  
ENV SPARK_HOME /usr/local/spark-${SPARK_VERSION}  
  
ENV PATH $PATH:${SPARK_HOME}/bin  
RUN curl -sL --retry 3 \  
"http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \  
| gunzip \  
| tar x -C /usr/local \  
&& mv /usr/local/$SPARK_PACKAGE $SPARK_HOME \  
&& ln -s $SPARK_HOME /usr/local/spark \  
&& chown -R root:root $SPARK_HOME  
ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH  
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH  
  
# Airflow  
ENV AIRFLOW_HOME /root/volume/airflow  
VOLUME /root/volume  
  
EXPOSE 8080  
WORKDIR /root/volume  
ENTRYPOINT ["./run_airflow.sh"]  
  

