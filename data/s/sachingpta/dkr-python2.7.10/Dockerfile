# Set the base image sachingpta/dkr-jdk-1.8.0_111  
FROM sachingpta/dkr-jdk-1.8.0_111  
  
# Author or maintainer of this image file  
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  
  
# All packages must work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
#-------------------------------------------------------------------  
# Install & check python 2.7.10  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV PYTHON_VERSION 2.7.10  
ENV PYTHON_DIR /Python-$PYTHON_VERSION  
RUN export PYTHON_VERSION=2.7.10  
RUN export PYTHON_DIR=/Python-$PYTHON_VERSION  
  
# Download zip file, extact, install python  
RUN wget
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
&& \  
tar xzf Python-$PYTHON_VERSION.tgz && \  
rm -rf Python-$PYTHON_VERSION.tgz && \  
cd Python-$PYTHON_VERSION && \  
sudo ./configure && \  
sudo make altinstall && \  
python2.7 --version  
  
# Install other python dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-dev \  
python-pip \  
python-virtualenv \  
&& rm -rf /var/lib/apt/lists/*  
  
# Verify installed version  
RUN python --version  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

