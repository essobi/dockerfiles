FROM onmodulus/run-base  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PHP_VER="5.6.23"  
ADD . /opt/modulus  
ENV PATH=/opt/modulus/bin:$PATH  
  
RUN /opt/modulus/bootstrap.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

