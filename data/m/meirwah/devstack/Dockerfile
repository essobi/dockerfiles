FROM ubuntu:14.04  
MAINTAINER Meir Wahnon  
  
RUN apt-get update -y  
  
RUN apt-get install git -y --fix-missing  
  
RUN apt-get update -qq && apt-get install -y python python-pip python-dev  
  
RUN git clone https://git.openstack.org/openstack-dev/devstack  
  
ADD local.conf devstack/  
  
WORKDIR devstack/tools/  
  
RUN ./create-stack-user.sh  
  
WORKDIR /devstack/  
  
RUN su -m stack ./stack.sh  

