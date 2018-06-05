FROM debian:wheezy  
  
MAINTAINER Romain Fihue <romain.fihue@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y wget python-software-properties  
  
RUN wget -k --no-check-certificate -O /tmp/puppetlabs-release-wheezy.deb
https://apt.puppetlabs.com/puppetlabs-release-wheezy.deb  
  
RUN dpkg -i /tmp/puppetlabs-release-wheezy.deb  
RUN apt-add-repository 'deb http://apt.puppetlabs.com wheezy devel' #Enable RC
repo  
  
RUN apt-get update  
  
RUN apt-get install -y puppet  

