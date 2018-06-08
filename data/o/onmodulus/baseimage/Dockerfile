FROM phusion/baseimage:0.9.18  
MAINTAINER Modulus <help@modulus.io>  
  
Add . /opt/modulus  
ENV PATH=/opt/modulus/bin:$PATH  
  
RUN /opt/modulus/bootstrap.sh  
  
ENV TEMP_DIR /mnt/tmp  
ENV TMPDIR /mnt/tmp  
ENV TMP_DIR /mnt/tmp  
ENV HOME /mnt/home  
  
CMD ["/sbin/my_init"]  

