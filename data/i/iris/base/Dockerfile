# Copyright (c) 2014 Project Iris. All rights reserved.  
#  
# The current Docker container is part of the official image collection of the  
# Iris cloud messaging system, and as such, the same licensing terms apply.  
# For details please see http://iris.karalabe.com/downloads#License  
# Base image for running an Iris node, with specific versions injected by the  
# bootstrapper script.  
FROM debian:7  
MAINTAINER Péter Szilágyi <peterke@gmail.com>  
  
# Pull in system updates and install required packages  
RUN \  
apt-get update && \  
apt-get install -y ca-certificates wget  
  
# Add helper scripts and define some default config values  
ADD scripts /scripts  
ENV IRIS_BIN /iris/bin/iris  
ENV IRIS_RSA /iris.rsa  
RUN \  
chmod -R +x /scripts && \  
mkdir -p `dirname $IRIS_BIN`  
  
# Set Iris as the entry point  
ENTRYPOINT ["/scripts/iris.sh"]  

