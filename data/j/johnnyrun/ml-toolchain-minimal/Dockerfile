FROM resin/i386-ubuntu:14.04  
MAINTAINER johnnyrun  
ADD terry_guo-gcc-arm-embedded-trusty.list /etc/apt/sources.list.d/terry_guo-
gcc-arm-embedded-trusty.list  
RUN apt-get update  
RUN apt-get -y install build-essential vim mercurial python zip python-
docutils sudo  
RUN apt-get -y --force-yes install gcc-arm-none-eabi make wget  
RUN echo 'PS1="ML_build\\[\033[01;34m\\] \w \$\\[\033[00m\\]"' >>
/etc/bash.bashrc  
RUN mkdir /ml  
RUN rm /etc/skel/.bashrc  
RUN rm /root/.bashrc  
RUN apt-get clean  

