FROM ubuntu:14.04  
MAINTAINER Jordan Wesolowski <jrwesolo@gmail.com>  
  
RUN echo 'Etc/UTC' > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Chaining these commands to reduce layers/size  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y curl lsof passwd sudo && \  
apt-get clean  
  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  

