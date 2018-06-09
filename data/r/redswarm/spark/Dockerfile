FROM debian:stable  
MAINTAINER Michael Kaldawi <mkaldawi@gmail.com>  
LABEL Description="This image runs Spark on debian."  
  
RUN apt-get update && apt-get install -y \  
wget \  
default-jdk \  
git  
  
RUN wget http://www.scala-lang.org/files/archive/scala-2.10.4.tgz  
RUN mkdir /usr/local/src/scala  
RUN tar xvf scala-2.10.4.tgz -C /usr/local/src/scala/  
RUN rm scala-2.10.4.tgz  
  
RUN wget http://apache.cs.utah.edu/spark/spark-1.4.0/spark-1.4.0.tgz  
RUN tar -xzf spark-1.4.0.tgz  
RUN rm spark-1.4.0.tgz  
RUN cd spark-1.4.0  

