################################################################################  
##################### Set Inital Image to work from
############################  
FROM ubuntu:16.04  
  
################################################################################  
##################### Add Container Labels
#####################################  
LABEL "Description"="Software toolkit for T/B cell repertoire"  
  
################################################################################  
############## set environment variables
#######################################  
  
ENV version 2.1.10  
  
################################################################################  
##################### Install System Dependencies
##############################  
RUN apt-get update -y && apt-get install -y \  
git \  
build-essential \  
openjdk-8-jre \  
wget \  
unzip  
  
################################################################################  
##################### Install MIXCR #########################################  
  
# set inital WORKDIR  
WORKDIR /mixcr/  
  
# download the source  
RUN wget
https://github.com/milaboratory/mixcr/releases/download/v${version}/mixcr-${version}.zip  
  
# unzip the source  
RUN unzip mixcr-${version}.zip  
  
################################################################################  
###################### set environment path #################################  
  
# add mixcr executable to path  
ENV PATH="/mixcr/mixcr-${version}/:${PATH}"  

