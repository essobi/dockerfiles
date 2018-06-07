FROM phusion/baseimage:0.9.16  
MAINTAINER Enderson Maia <endersonmaia@gmail.com>  
  
ADD . /build  
  
RUN /build/install.sh && \  
/build/cleanup.sh  
  
CMD ["/sbin/my_init"]  
  
EXPOSE 80

