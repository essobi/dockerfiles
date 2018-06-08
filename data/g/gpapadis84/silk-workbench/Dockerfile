FROM ubuntu:14.04  
MAINTAINER George Papadakis <gpapadis@di.uoa.gr>  
  
RUN apt-get update && apt-get install -y \  
default-jdk \  
wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN wget https://github.com/silk-
framework/silk/releases/download/release-2.6.1/silk-workbench-2.6.1.tgz && \  
tar zxvf silk-workbench-2.6.1.tgz && \  
rm -Rf /silk-workbench--2.6.1.tgz && \  
./silk-workbench-2.6.1/bin/silk-workbench  

