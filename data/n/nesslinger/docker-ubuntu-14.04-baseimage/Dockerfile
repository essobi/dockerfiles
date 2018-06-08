# Docker file based on Ubuntu 14.04 image with some additional tools  
FROM ubuntu:14.04  
MAINTAINER Michael Neßlinger <Michael.Nesslinger@gmx.de>  
  
# enable noninteractive mode  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# update sources before installing additional tools  
RUN apt-get -q -y update  
  
# install some additional tools  
RUN apt-get -q -y install software-properties-common curl nano unzip
subversion git  
  
# cleanup  
RUN apt-get clean  
  
# use the good old bash as default command  
CMD ["bash"]

