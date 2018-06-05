FROM phusion/baseimage:latest  
MAINTAINER David Young <davidy@funkypenguin.co.nz>  
#Based on the work of needo <needo@superhero.org>  
#  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Add a generic htpc user, which we'll reuse for all HTPC containers, and set
UID predictable value (the meaning of 2 lives)  
RUN useradd htpc -u 4242  
  
ADD setupcron.sh /etc/my_init.d/setupcron.sh  
RUN chmod +x /etc/service/*/run /etc/my_init.d/*  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
  
VOLUME /config  

