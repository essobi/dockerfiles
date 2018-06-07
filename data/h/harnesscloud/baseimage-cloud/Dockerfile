FROM phusion/baseimage:latest  
MAINTAINER Mark Stillwell <mark@stillwell.me>  
  
RUN rm -f /etc/service/sshd/down  
COPY scripts/setkey.sh /etc/my_init.d/05-setkey  
RUN chmod 755 /etc/my_init.d/05-setkey  

