# Dockerfile for Base Image Creation  
# Ubuntu 13.10 (Saucy Salamander)  
# Built with Debianâs tool Debootstrap  
# See DOCKER index lgsd/saucy  
  
# VERSION 1.1  
  
# Apply Dockerfile Best Practices :  
#  
# 1\. Keep common instructions at the top of the  
# Dockerfile to utilize the cache.  
#  
# 2\. Always pass -t to tag the resulting image.  
#  
# 3\. Never map the public port in a Dockerfile.  
#  
# 4\. Always use the array syntax when using CMD  
# and ENTRYPOINT.  
#  
# 5\. ENTRYPOINT and CMD are better together.  
#  
# see http://crosbymichael.com/dockerfile-best-practices.html  
  
FROM lgsd/saucy  
  
MAINTAINER Luca G. Soave <luca.soave@gmail.com>  
  
# You can force a daily or weekly upgrade of all your  
# packages changing REFRESHED_AT date, from time to time  
# otherwise the first lines would be cached by docker and  
# you would always use non up-to-date versions of your OS  
  
ENV REFRESHED_AT 2013-12-03  
  
# make sure the package repository is up to date  
# for different ubuntu versions, eventually  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  

