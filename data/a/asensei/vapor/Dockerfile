FROM ubuntu:14.04  
# Set environment variables for image  
ENV UBUNTU_VERSION ubuntu14.04  
ENV UBUNTU_VERSION_NO_DOTS ubuntu1404  
ENV SHELL /bin/bash  
ENV HOME /vapor  
ENV WORK_DIR /vapor  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Linux OS utils and libraries  
RUN apt-get update && apt-get install -y \  
binutils \  
software-properties-common \  
python-software-properties \  
lsb-release \  
apt-transport-https \  
curl && \  
rm -r /var/lib/apt/lists/*  
  
# Install Vapor Toolbox  
RUN curl https://repo.vapor.codes/apt/keyring.gpg | apt-key add -  
RUN echo "deb https://repo.vapor.codes/apt $(lsb_release -sc) main" | tee
/etc/apt/sources.list.d/vapor.list  
RUN apt-get update && apt-get install -y \  
swift=4.1.0 \  
vapor=3.1.6  

