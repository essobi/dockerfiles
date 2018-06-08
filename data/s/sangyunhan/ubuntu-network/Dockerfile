FROM ubuntu:16.04  
MAINTAINER Sangyun Han <sangyun628@gmail.com>  
  
# run update  
RUN apt-get update  
  
# install network tool  
RUN apt-get install curl -y  
RUN apt-get install net-tools -y  
RUN apt-get install iputils-ping -y  
RUN apt-get install iperf -y  
RUN apt-get install htop -y  
RUN apt-get install traceroute -y  
RUN apt-get install nmap -y  
RUN apt-get install wget -y  
  
# For service  
CMD ping 127.0.0.1  

