FROM phusion/baseimage  
MAINTAINER rix1337  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Configure user nobody to match unRAID's settings  
RUN \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
RUN apt-get update && apt-get -y install wget python  
  
COPY root/ /  
RUN chmod +x /etc/my_init.d/*.sh && chmod +x /version.py  
  
VOLUME /config  
EXPOSE 53/tcp 53/udp  

