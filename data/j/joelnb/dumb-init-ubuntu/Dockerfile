FROM ubuntu:trusty  
MAINTAINER Joel Noyce Barnham <joelnbarnham@gmail.com>  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
build-essential \  
python-dev \  
python-pip \  
&& \  
pip install dumb-init && \  
apt-get remove -y \  
build-essential \  
python-dev \  
python-pip \  
&& \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
:  
  
ENTRYPOINT ["dumb-init"]  

