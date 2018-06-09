FROM phusion/baseimage:0.9.11  
MAINTAINER talenddev <leo@talenddev.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
# add user  
RUN useradd --no-create-home -g users \--uid 22000 share  
  
CMD ["/sbin/my_init"]  

