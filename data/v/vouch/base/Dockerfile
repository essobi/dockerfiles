FROM ubuntu:trusty  
MAINTAINER Ben Yee <ben@vouch.com>  
  
# Install deps  
RUN apt-get update  
RUN apt-get clean  
RUN apt-get install -y autoconf bison build-essential libssl-dev libyaml-dev
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev
libxml2-dev libpq-dev  
RUN apt-get install -y git curl  
ENV HOME /home  

