FROM ubuntu:16.10  
  
RUN apt-get update  
  
RUN apt-get -y upgrade  
  
RUN apt-get install -y software-properties-common  
  
RUN add-apt-repository ppa:saiarcot895/myppa  
RUN apt-get update  
RUN apt-get -y install apt-fast  
  
RUN apt-fast -y install apt-utils apt-transport-https python-software-
properties curl git  
  
# Cache is kept so sub-containers don't need to reload the cache  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

