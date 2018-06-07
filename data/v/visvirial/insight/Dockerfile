####################################################################################################  
# Dockerfile for insight.  
# @author Vis Virial <visvirial@gmail.com>  
####################################################################################################  
  
FROM ubuntu:trusty  
MAINTAINER Vis Virial <visvirial@gmail.com>  
  
##################################################  
  
# Change package repo.  
RUN cp /etc/apt/sources.list /etc/apt/sources.list.old && \  
sed -e "s/http:\/\/archive.ubuntu.com/http:\/\/jp.archive.ubuntu.com/g"
/etc/apt/sources.list.old >/etc/apt/sources.list  
  
# Refresh repo.  
RUN apt-get -q --yes update && apt-get -q --yes upgrade  
  
##################################################  
  
# Add apt-add-repository  
RUN apt-get -q --yes install software-properties-common  
  
# Add Node.js repository and install it.  
RUN apt-add-repository --yes ppa:chris-lea/node.js && apt-get -q --yes update
&& apt-get -q --yes install nodejs  
  
##################################################  
  
# Install required packages.  
RUN apt-get -q --yes install git python build-essential  
  
##################################################  
  
# Create user.  
RUN adduser docker  
  
# Change user.  
USER docker  
WORKDIR /home/docker  
ENV HOME /home/docker  
  
##################################################  
  
# Cloning from git.  
RUN git clone https://github.com/bitpay/insight.git  
  
# Install dependencies.  
RUN cd insight && npm install  
  
##################################################  
##################################################  
##################################################  
  
ENTRYPOINT cd insight && npm start  
  

