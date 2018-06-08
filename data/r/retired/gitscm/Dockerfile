FROM ubuntu:14.04  
RUN apt-get -qq update  
RUN apt-get -qqy install \  
git  
  
ENV HOME /home  
  
RUN apt-get -qqy autoremove  
RUN apt-get -qqy clean  
  
ENTRYPOINT /bin/bash  

