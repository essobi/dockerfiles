#Dockerfile for deploying bookkeeper-nvm  
FROM ubuntu:14.04  
MAINTAINER Jaln Liu <jaln.liu@ttu.edu>  
RUN apt-get update  
RUN apt-get install -y default-jdk  
RUN apt-get install -y maven  
RUN apt-get install -y git  
RUN git clone https://valiantljk@bitbucket.org/valiantljk/bookkeeper-nvm.git  
  
#Configure Environments  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
ENV PATH $JAVA_HOME/bin:$PATH  
  
#Install bookkeeper  
RUN cd /bookkeeper-nvm && mvn clean && mvn compile -DskipTests && mvn install
-DskipTests  
#Specify Journal/Ledger Location  
RUN mkdir /bookdir&& mkdir /bookdir/bktest && mkdir bookdir/bktest/journals &&
mkdir /bookdir/bktest/ledgers  

