#DOCKERFILE FOR BIONODE-NCBI  
FROM ubuntu:16.04  
MAINTAINER Bruno Gonçalves, bfgoncalves@medicina.ulisboa.pt  
  
#SET WORKDIR  
WORKDIR /NGStools/  
#INSTALL DEPENDENCIES  
RUN apt-get update  
RUN apt-get install -y curl sudo  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
RUN npm install bionode -g  

