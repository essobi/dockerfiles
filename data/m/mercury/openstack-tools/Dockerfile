FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Go/Packer prerequisite, ansible, and openstack packages  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-utils \  
software-properties-common \  
&& apt-get install -y --no-install-recommends \  
gcc \  
git \  
python3-dev \  
python3-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install glancecp  
RUN mkdir /tmp/openstack-tools  
ADD . /tmp/openstack-tools  
RUN cd /tmp/openstack-tools \  
&& python3 setup.py install  
RUN rm -rf /tmp/openstack-tools  
  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

