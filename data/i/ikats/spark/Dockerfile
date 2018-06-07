FROM ubuntu:xenial  
  
LABEL license="Apache License, Version 2.0"  
LABEL copyright="CS Systèmes d'Information"  
LABEL maintainer="contact@ikats.org"  
LABEL version="0.7.39"  
  
# Note, we use spark 1.6.1 as it is the version that was present on the  
# codebase, but there is avaliable release for all the other versions.  
# (Including those >= 2.X)  
# Install python3  
RUN apt-get update \  
&& apt-get install -y \  
python3 \  
curl \  
unzip \  
python3-setuptools \  
build-essential \  
python3 \  
python3-dev \  
python3-pip \  
libffi-dev \  
scala \  
openssl \  
git \  
libpq-dev \  
&& ln -s /usr/bin/python3 /usr/bin/python \  
&& easy_install3 pip py4j \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Spark  
ENV SPARK_VERSION=1.6.1  
ENV HADOOP_VERSION=2.6  
ENV SPARK_HOME /opt/spark  
  
  
ADD
https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz /  
  
RUN tar xvf /spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \  
&& mv /spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} \  
&& rm /spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz  
  
# Install Java  
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
  
ADD assets/spark-defaults.conf /opt/spark/conf/  
  
ADD assets/start_spark.sh /  
  
# Spark  
EXPOSE 7077 8080 8081 4040  
ENTRYPOINT ["bash", "/start_spark.sh"]  

