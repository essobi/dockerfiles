FROM phusion/baseimage:0.9.18  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
ENV HOME /root  
  
CMD ["/sbin/my_init"]  
  
# Install wget  
RUN apt-get update && apt-get install -y wget  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

