FROM ubuntu:14.04  
MAINTAINER Ash Wilson  
  
RUN apt-get update && apt-get install -y git vim wget  
  
WORKDIR /root  
  
RUN wget -P /tmp https://opscode-omnibus-
packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chefdk_0.10.0-1_amd64.deb &&
dpkg -i /tmp/chefdk_0.10.0-1_amd64.deb  
  
CMD /bin/bash  

