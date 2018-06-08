FROM onmodulus/build-base  
  
ADD . /opt/modulus  
RUN /opt/modulus/bootstrap.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

