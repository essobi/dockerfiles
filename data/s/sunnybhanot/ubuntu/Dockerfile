####  
#  
# Dockerfile for Ubuntu Trusty Tahr  
#  
###  
FROM ubuntu:trusty  
  
# Install  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y \  
build-essential \  
software-properties-common \  
python2.7 \  
byobu \  
curl \  
git \  
htop \  
man \  
unzip \  
vim \  
wget \  
&& ln -s /usr/bin/python2.7 /usr/bin/python \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set Enviroment Variable  
ENV HOME /root  
  
# Working directory  
WORKDIR /root  
  
# Default Command  
CMD ["bash"]  

