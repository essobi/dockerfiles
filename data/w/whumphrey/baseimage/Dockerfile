FROM ubuntu:trusty  
MAINTAINER Wayne Humphrey <wayne@humphrey.za.net>  
LABEL version="1.1"  
  
# Set system the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Set some env variables as we mostly work in non interactive mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Update system and install Supervisord and OpenSSH server  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt-get install supervisor openssh-server -y -o Dpkg::Options::="--force-
confold"  
  
# Add image init and supervisord config  
ADD helper/init /sbin/init  
ADD helper/init_user /sbin/init_user  
ADD helper/supervisord.conf /etc/supervisor/supervisord.conf  
RUN chmod 755 /sbin/init /sbin/init_user  
  
# Create and configure vagrant user  
# see https://hub.docker.com/r/fgrehm/vagrant-ubuntu/~/dockerfile/  
# Set root password to toor  
RUN echo 'root:toor' | chpasswd  
  
# Enable passwordless sudo for users under the "sudo" group  
RUN sed 's/%sudo\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%sudo ALL=NOPASSWD:ALL/g'
-i /etc/sudoers  
  
EXPOSE 22 80 3306 9001  
# Use baseimage-docker's init system.  
CMD ["/sbin/init"]  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

