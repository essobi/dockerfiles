# Download and install Matlab Compiler Runtime v9.3 (2017b)  
#  
# This docker file will configure an environment into which the Matlab
compiler  
# runtime will be installed and in which stand-alone matlab routines (such as  
# those created with Matlab's deploytool) can be executed.  
#  
# See http://www.mathworks.com/products/compiler/mcr/ for more info.  
  
FROM debian:stretch-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && \  
apt-get install -q -y \--no-install-recommends \  
xorg \  
unzip \  
wget \  
curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install the MCR dependencies and some things we'll need and download the MCR  
# from Mathworks -silently install it  
RUN mkdir /mcr-install && \  
mkdir /opt/mcr && \  
cd /mcr-install && \  
wget -q
http://ssd.mathworks.com/supportfiles/downloads/R2017b/deployment_files/R2017b/installers/glnxa64/MCR_R2017b_glnxa64_installer.zip
&& \  
unzip -q MCR_R2017b_glnxa64_installer.zip && \  
rm -f MCR_R2017b_glnxa64_installer.zip && \  
./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \  
cd / && \  
rm -rf mcr-install  
  
# Configure environment variables for MCR  
ENV LD_LIBRARY_PATH
/opt/mcr/v93/runtime/glnxa64:/opt/mcr/v93/bin/glnxa64:/opt/mcr/v93/sys/os/glnxa64  
ENV XAPPLRESDIR /opt/mcr/v93/X11/app-defaults

