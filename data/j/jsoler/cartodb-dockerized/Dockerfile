FROM ubuntu:precise  
#12.04 x64  
RUN locale-gen en_US.UTF-8 && update-locale  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install autoconf binutils-doc bison build-
essential flex git python-software-properties  

