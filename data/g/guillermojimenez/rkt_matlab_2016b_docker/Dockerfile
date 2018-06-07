# From the original work of Michael Perry, Stanford University.  
# https://github.com/vistalab/docker/tree/master/matlab/runtime/2014b  
#  
# This docker file will configure an environment into which the Matlab
compiler  
# runtime will be installed and in which stand-alone matlab routines (such as  
# those created with Matlab's deploytool) can be executed.  
#  
# See http://www.mathworks.com/products/compiler/mcr/ for more info.  
  
FROM ubuntu:latest  
  
MAINTAINER guillermo.jimenez@upf.edu  
  
RUN apt-get -qq update && apt-get -qq install -y \  
unzip \  
wget \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install the MCR dependencies and some things we'll need and download the MCR  
# from Mathworks -silently install it  
RUN mkdir /mcr-install \  
&& mkdir /opt/mcr \  
&& cd /mcr-install \  
&& wget
https://es.mathworks.com/supportfiles/downloads/R2016b/deployment_files/R2016b/installers/glnxa64/MCR_R2016b_glnxa64_installer.zip
\  
&& cd /mcr-install \  
&& unzip -q MCR_R2016b_glnxa64_installer.zip \  
&& ./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent \  
&& cd / \  
&& rm -rf mcr-install  
  
  
# Configure environment variables for MCR  
ENV LD_LIBRARY_PATH
/opt/mcr/v91/runtime/glnxa64:/opt/mcr/v91/bin/glnxa64:/opt/mcr/v91/sys/os/glnxa64  
ENV XAPPLRESDIR /opt/mcr/v91/X11/app-defaults  

