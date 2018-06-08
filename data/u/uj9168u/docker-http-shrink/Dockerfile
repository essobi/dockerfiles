FROM ubuntu  
MAINTAINER Chih Lun Liu <s100061134@m100.nthu.edu.tw>  
RUN apt-get update && \  
apt-get install -y wget curl net-tools build-essential tar git nano dialog &&
\  
apt-get install -y python python-dev python-distribute python-pip && \  
mkdir /root/HttpServer && \  
cd /root/HttpServer && \  
echo 'python -m SimpleHTTPServer 80' > /etc/bash.bashrc  
EXPOSE 80  

