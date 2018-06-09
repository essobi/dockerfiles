FROM phusion/baseimage:latest  
MAINTAINER Tomas Jacik <tomas@jacik.cz>  
  
ADD . /build  
  
RUN /build/prepare.sh && \  
/build/system_services.sh && \  
/build/cleanup.sh  
  
CMD ["/sbin/my_init"]  

