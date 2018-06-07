FROM ubuntu:14.04.3  
MAINTAINER Eric Johnson <eric.johnson@mycase.com>  
  
RUN apt-get -yqq update  
RUN apt-get -yqq install curl lsb-release  
RUN curl -L https://getchef.com/chef/install.sh | bash -s -- -v 12.5.1  
RUN apt-get -yqq clean  
  

