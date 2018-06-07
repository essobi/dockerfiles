FROM ubuntu:16.04  
MAINTAINER Tomas Jacik <tomas@jacik.cz>  
  
ADD . /bd_build  
  
RUN /bd_build/prepare.sh && \  
/bd_build/system_services.sh && \  
/bd_build/utilities.sh && \  
/bd_build/cleanup.sh  
  
CMD ["/sbin/my_init"]  

