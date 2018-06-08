FROM ubuntu:trusty  
MAINTAINER Chih Lun Liu <s100061134@m100.nthu.edu.tw>  
RUN apt-get update && \  
apt-get install -y wget curl net-tools build-essential tar git nano dialog
python python-dev python-distribute python-pip && \  
  
mkdir /root/HttpServer && \  
  
cd /root/HttpServer && \  
echo 'python -m SimpleHTTPServer 80' > /etc/bash.bashrc && \  
apt-get remove -y \--auto-remove wget curl net-tools tart git nano dialog && \  
apt-get clean  
  
  
EXPOSE 80  

