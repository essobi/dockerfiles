FROM phusion/baseimage:0.9.17  
MAINTAINER rwohleb <rob@tispork.com>  
# FORK FROM PDucharme-Plexconnect on GitHub  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Install PlexConnect  
ADD install.sh /  
RUN bash /install.sh  
  
VOLUME /config  
  
EXPOSE 80 443 53  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  

