FROM ubuntu:16.04  
  
ADD apt.conf /etc/apt/apt.conf.d/99norecommends  
  
RUN apt-get -y update && apt-get autoremove -y  
RUN apt-get -y install git libmicrohttpd-dev libssl-dev cmake build-essential
libhwloc-dev  

