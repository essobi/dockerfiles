#  
# Dockerfile  
#  
# Copyright (c) 2015-2016 Junpei Kawamoto  
#  
# This software is released under the MIT License.  
#  
# http://opensource.org/licenses/mit-license.php  
#  
FROM ubuntu:latest  
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM vt100  
  
RUN apt-get update && \  
apt-get install -y apt-utils python python-pip python-dev wget curl git ssh-
client graphviz && \  
apt-get upgrade -y && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/  
RUN pip install --upgrade pip ghp-import  

