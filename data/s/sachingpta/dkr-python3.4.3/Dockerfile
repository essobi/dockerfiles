# Set the base image sachingpta/dkr-python2.7.10  
FROM sachingpta/dkr-python2.7.10  
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
# Install & check python 3.4.3  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV PYTHON3_VERSION 3.4.3  
ENV PYTHON3_DIR /Python-$PYTHON3_VERSION  
RUN export PYTHON3_VERSION=3.4.3  
RUN export PYTHON3_DIR=/Python-$PYTHON3_VERSION  
  
# Download zip file, extact, install python  
RUN wget
https://www.python.org/ftp/python/$PYTHON3_VERSION/Python-$PYTHON3_VERSION.tgz
&& \  
tar xzf Python-$PYTHON3_VERSION.tgz && \  
rm -rf Python-$PYTHON3_VERSION.tgz && \  
cd Python-$PYTHON3_VERSION && \  
sudo ./configure && \  
sudo make altinstall && \  
python3.4 --version  
  
# Install other python dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python3-dev \  
python3-pip \  
python3-virtualenv \  
&& rm -rf /var/lib/apt/lists/*  
  
# Verify installed version  
RUN python3 --version  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

