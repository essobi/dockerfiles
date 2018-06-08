# jmvrbanac/multi-mechanize  
#  
# Docker image for running multi-mechanize  
#  
FROM ubuntu:latest  
MAINTAINER John Vrbanac <john.vrbanac@linux.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update; apt-get install -y vim git python-pip python-dev python-
matplotlib  
  
# Install text-based browser for looking at the results  
RUN apt-get install -y elinks  
  
RUN pip install multi-mechanize  
  
CMD ["bash"]  

