FROM ubuntu:14.04  
MAINTAINER Shane Logsdon <shane@shanelogsdon.com>  
  
RUN apt-get update  
RUN sudo apt-get install -y software-properties-common build-essential  
RUN sudo add-apt-repository ppa:hansjorg/rust  
RUN apt-get update  
RUN sudo apt-get install -y --force-yes rust-0.10  

