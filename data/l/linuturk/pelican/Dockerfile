FROM ubuntu:14.04  
MAINTAINER Justin Phelps <linuturk@onitato.com>  
  
# Set various options  
USER root  
WORKDIR /root  
  
# Update OS  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Fix locale  
RUN locale-gen en_US.UTF-8  
  
# Install Ansible  
RUN apt-get install git build-essential python-dev python-pip -y  
RUN pip install pelican Markdown  

