############################################################  
# This is a Dockerfile to build and deploy a Radium node  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:latest  
  
# Docker author  
MAINTAINER Tim Mesker [tm2013@projectradium.org]  
  
# Update the repository sources list  
RUN apt-get -y update  
  
################## BEGIN INSTALLATION ######################  
# Install process for deploying a Radium node, pursuant to Bitcoin client
standards  
  
# Install dependencies  
RUN apt-get -y install git build-essential libssl-dev libdb++-dev libboost-
all-dev libqrencode-dev libminiupnpc-dev qt5-default qt5-qmake qtbase5-dev-
tools qttools5-dev-tools  
  
# Clone the Radium source code from Github  
RUN git clone https://github.com/ProjectRadium/Radium.git && cd Radium  
  
# Specify the correct volume  
VOLUME /Radium  
  
# Expose the default RPC and P2P port  
EXPOSE 27913 27914  
  
# Specify the correct working directory  
WORKDIR /Radium  
  
# Build Radium-qt and Radiumd  
ENTRYPOINT qmake USE_03=1 RELEASE=1 && make && cd src && make -f makefile.unix
&& strip Radiumd  
  
##################### INSTALLATION END #####################  

