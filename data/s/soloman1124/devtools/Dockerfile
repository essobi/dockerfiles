FROM phusion/baseimage:latest  
MAINTAINER Soloman Weng <soloman1124@gmail.com>  
  
CMD ["/sbin/my_init"]  
  
ADD ./install /install  
WORKDIR /install  
RUN ./install.sh  
RUN rm -rf /install  
  
ENV PATH=/go/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p /usr/src/app && chown app:app /usr/src/app  
WORKDIR /usr/src/app  

