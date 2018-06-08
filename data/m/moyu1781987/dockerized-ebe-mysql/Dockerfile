# Dockerfile for creating mysql server and populate data  
# Written by: Xiaowen Zhang  
# Built from mysql:5.7  
FROM mysql:5.7  
MAINTAINER Xiaowen Zhang <seanxwzhang@gmail.com>  
ENV MYSQL_ROOT_PASSWORD abc123456  
  
# Mount the current directory  
ADD ./dbconfig.sh /bin/dbconfig.sh  
  
# Install necessary software  
RUN apt-get update \  
&& apt-get install -y wget pv vim python  
  
# Make sure time is correct when pulling data dump  
Run echo "America/Los_Angeles" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata  

