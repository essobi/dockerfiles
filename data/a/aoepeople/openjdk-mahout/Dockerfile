FROM openjdk:alpine  
  
USER root  
  
RUN apk add --no-cache bash  
  
ENV MAHOUT_VERSION 0.13.0  
ENV HADOOP_VERSION 2.7.3  
ENV MAHOUT_LOCAL true  
ENV MAHOUT_HOME /usr/local/mahout  
ENV HADOOP_HOME /usr/local/hadoop  
ENV JAVA_HOME /usr  
  
WORKDIR /tmp  
  
RUN wget --no-verbose
"http://archive.apache.org/dist/mahout/${MAHOUT_VERSION}/apache-mahout-
distribution-${MAHOUT_VERSION}.tar.gz" && tar -xzf "apache-mahout-
distribution-${MAHOUT_VERSION}.tar.gz" && rm "apache-mahout-
distribution-${MAHOUT_VERSION}.tar.gz" && mv "apache-mahout-
distribution-${MAHOUT_VERSION}" ${MAHOUT_HOME}  
RUN wget --no-verbose
"http://archive.apache.org/dist/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"
&& tar -xzf "hadoop-${HADOOP_VERSION}.tar.gz" && rm
"hadoop-${HADOOP_VERSION}.tar.gz" && mv "hadoop-${HADOOP_VERSION}"
${HADOOP_HOME}  
  
WORKDIR /opt/docker  

