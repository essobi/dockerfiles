FROM ubuntu:14.04  
MAINTAINER Niels Braczek <nbraczek@bsds.de>  
  
ADD . /build.d  
  
RUN /build.d/prepare.sh && \  
/build.d/system_services.sh && \  
/build.d/utilities.sh && \  
/build.d/cleanup.sh  
  
CMD ["/sbin/my_init"]  

