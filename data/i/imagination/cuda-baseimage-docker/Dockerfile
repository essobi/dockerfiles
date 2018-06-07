FROM nvidia/cuda:7.5-cudnn3-devel-ubuntu14.04  
MAINTAINER Phusion <info@phusion.nl>  
  
ADD . /bd_build  
  
RUN /bd_build/prepare.sh && \  
/bd_build/system_services.sh && \  
/bd_build/utilities.sh && \  
/bd_build/cleanup.sh  
  
CMD ["/sbin/my_init"]  

