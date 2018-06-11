FROM ubuntu:trusty  
MAINTAINER Martin Grønlien Pejcoch <mpejcoch@gmail.com>  
  
RUN /usr/bin/gpg --keyserver pgp.mit.edu --recv-keys 989BA1EB && /usr/bin/gpg
-a --export 989BA1EB | /usr/bin/apt-key add -  
  
ADD heiko.list /etc/apt/sources.list.d/  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install libfimex-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install git  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install build-essential
libtool pkg-config autoconf  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install vim  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install cmake  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install apt-utils  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install unzip wget  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install qt4-dev-tools
devscripts debhelper  

