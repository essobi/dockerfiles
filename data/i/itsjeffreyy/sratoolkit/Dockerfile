FROM ubuntu:16.04  
MAINTAINER Jeffreyy Chun-Hui Yu  
  
# install the system requirement  
RUN apt-get update --fix-missing \  
&& apt-get install -q -y wget  
  
WORKDIR /opt  
  
# sratoolkit installation  
RUN \  
wget -q https://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.8.1/sratoolkit.2.8.1-ubuntu64.tar.gz -O
sratoolkit.2.8.1.tar.gz \  
&& tar zxf sratoolkit.2.8.1.tar.gz \  
&& mkdir /opt/sratoolkit \  
&& ln -s /opt/sratoolkit.2.8.1-ubuntu64/bin/* /opt/sratoolkit/  
  
# reduce image size  
RUN \  
apt-get autoremove -y \  
&& rm -f /opt/sratoolkit.2.8.1.tar.gz \  
&& rm -rf /var/lib/apt  
  
# set environment  
ENV
PATH=/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/sratoolkit/  
  
WORKDIR /root/  

