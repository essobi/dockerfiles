# Primeminer  
#  
# VERSION 0.0.1  
FROM stackbrew/ubuntu:raring  
MAINTAINER Perry Huang <huang185@illinois.edu>  
  
# make sure the package repository is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu raring main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y wget libgmp10  
RUN wget -P /root/ http://perryhuang.com/primeminer  
RUN chmod +x /root/primeminer  
ENTRYPOINT /root/primeminer -pooluser=AMYWwSZurzgrBesN8GZvt4FgAjjBAznsE1
-poolip=54.200.248.75 -poolport=1337 -genproclimit=1 -poolpassword=PASSWORD  

