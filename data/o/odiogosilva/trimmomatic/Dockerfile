# DOCKERFILE for trimmomatic  
FROM ubuntu:16.04  
MAINTAINER Diogo N. Silva, diogosilva@medicina.ulisboa.pt  
  
RUN apt-get update && apt-get -y install \  
python3 \  
openjdk-8-jre \  
unzip  
  
ADD
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
/NGStools/  
  
WORKDIR /NGStools  
  
RUN unzip Trimmomatic-0.36.zip  
WORKDIR /NGStools/Trimmomatic-0.36  
  
RUN mv trimmomatic-0.36.jar trimmomatic.jar  

