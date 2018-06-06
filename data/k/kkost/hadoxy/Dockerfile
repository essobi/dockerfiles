FROM phusion/baseimage  
MAINTAINER kkost  
  
ENV HOME /root  
RUN mkdir /build  
ADD . /build  
RUN /build/install.sh  
RUN rm -f /etc/service/haproxy/down /etc/service/docker-gen/down  
CMD ["/sbin/my_init"]  

