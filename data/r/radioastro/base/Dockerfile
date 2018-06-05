FROM ubuntu:14.04  
MAINTAINER gijs@pythonic.nl  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# enable universe, multiverse, restricted with world wide mirrors  
ADD apt.sources.list /etc/apt/sources.list  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
software-properties-common \  
python-software-properties \  
python-pip \  
&& \  
add-apt-repository -y ppa:radio-astro/main && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# upgrade the pip package to the latest version  
RUN pip install --upgrade pip  

