FROM debian:jessie  
MAINTAINER Logan Attwood <logan@jnickel.com>  
  
ADD . /bd_build  
  
RUN /bd_build/prepare.sh && \  
/bd_build/system_services.sh && \  
/bd_build/utilities.sh && \  
/bd_build/cleanup.sh  
  
CMD ["/sbin/my_init"]  

