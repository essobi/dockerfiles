############################################################  
# Dockerfile to build lofreq variant caller container  
# Based on Ubuntu  
#  
# lofreq is on the path  
#  
# usage:  
# docker run seandavi/lofreq lofreq ....  
#  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Sean Davis <seandavi@gmail.com>  
  
# Update the repository sources list  
RUN apt-get update  
RUN apt-get install -y curl python  
  
RUN curl -L
'http://downloads.sourceforge.net/project/lofreq/lofreq_star-2.1.2_linux-x86-64.tgz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Flofreq%2Ffiles%2F&ts=1471618612&use_mirror=heanet'
> lofreq_star-2.1.2_linux-x86-64.tgz  
  
  
  
RUN tar -xvzf lofreq_star-2.1.2_linux-x86-64.tgz  
  
RUN cp lofreq_star-2.1.2/bin/* /usr/local/bin/  

