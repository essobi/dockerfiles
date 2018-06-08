FROM ubuntu:14.04  
MAINTAINER Ben Jones <ben@fogbutter.com>  
RUN apt-get update && \  
apt-get autoremove -y && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common aptitude && \  
apt-add-repository -y ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible  

