FROM phusion/baseimage:latest  
MAINTAINER Scott Kelly  
RUN apt-get -q update  
RUN apt-get install -y -q software-properties-common python-software-
properties  
RUN add-apt-repository ppa:saltstack/salt  
RUN apt-get -q update  
RUN apt-get install -y -q salt-minion  
  
CMD ["/sbin/my_init"]  
  

