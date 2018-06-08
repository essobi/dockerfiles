FROM centos  
  
MAINTAINER Tushar Pokle <tushar.pokle@gmail.com>  
  
  
RUN yum install -y unzip  
  
ADD https://dl.bintray.com/mitchellh/serf/0.4.1_linux_amd64.zip /tmp/serf.zip  
RUN unzip -d /usr/local/bin/ /tmp/serf.zip  
  
CMD serf agent  

