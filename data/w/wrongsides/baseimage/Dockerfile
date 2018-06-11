FROM phusion/baseimage:0.9.17  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN useradd --no-create-home -g users \--uid 1000 jarvis  
  
CMD ["/sbin/my_init"]  

