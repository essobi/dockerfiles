FROM ubuntu:14.04  
MAINTAINER George Papadakis <gpapadis@di.uoa.gr>  
  
ENV SILK_VERSION 2.6.1  
RUN apt-get update && \  
apt-get install -y \  
default-jdk \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://github.com/silk-
framework/silk/releases/download/release-${SILK_VERSION}/silk-
workbench-${SILK_VERSION}.tgz && \  
tar zxvf silk-workbench-${SILK_VERSION}.tgz && \  
rm -Rf /silk-workbench-${SILK_VERSION}.tgz  
  
CMD ["/bin/bash", "/silk-workbench-2.6.1/bin/silk-workbench"]  

