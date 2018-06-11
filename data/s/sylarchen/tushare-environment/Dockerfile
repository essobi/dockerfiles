FROM continuumio/anaconda3:4.1.1  
MAINTAINER Sylar Chen  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y vim curl wget  
  
#RUN pip --proxy http://web-proxy.atl.hp.com:8080 install tushare==0.5.0  
RUN pip install tushare==0.5.0  

