############################################################  
# Dockerfile to build base image used by my other images  
############################################################  
  
FROM phusion/baseimage:0.9.15  
  
MAINTAINER Wenbin Fang <wenbin@cs.wisc.edu>  
  
RUN /usr/sbin/enable_insecure_key  
  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/root/run"]  
  
ADD run /root/run  
RUN chmod 755 /root/run  
  
# Clean up.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

