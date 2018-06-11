FROM phusion/baseimage:latest  
MAINTAINER Daniel Miller <watermelonpizza@melonstudios.net>  
  
CMD ["/sbin/my_init"]  
  
RUN apt update && \  
apt install git -y && \  
git config --global push.default simple && \  
apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

