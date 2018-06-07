FROM phusion/baseimage:0.9.11  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
ENV HOME /root  
CMD ["/sbin/my_init"]  
ADD assets /opt/hopsoft/nginx  
RUN /opt/hopsoft/nginx/bin/build  

