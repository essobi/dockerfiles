# Start with Ubuntu base image  
FROM ubuntu:latest  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
# Using yun-idc mirror  
# RUN sed -i 's/http:\/\/archive\\.ubuntu\\.com/http:\/\/mirrors\\.yun-
idc\\.com/g' /etc/apt/sources.list  
# Upgrade to newest  
RUN apt-get update && apt-get upgrade -y  
  
# Upgrade to newest for children images  
ONBUILD \  
RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential
bash-completion  
  
CMD ["/bin/bash"]  

