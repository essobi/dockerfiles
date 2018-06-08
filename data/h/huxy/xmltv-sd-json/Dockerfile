# This is a comment  
FROM huxy/docker-debian:latest  
MAINTAINER James Huxtable <docker@codeape.co.uk>  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/my_init"]  
  
# Exclude Documentation  
ADD files/etc/dpkg/dpkg.cfg.d/01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
#set config directory  
VOLUME /config \  
/data \  
/unraid  
  
ADD files/bin/setup.sh /setup.sh  
RUN /setup.sh && rm /setup.sh  
  
# Add firstrun.sh to execute during container startup  
ADD files/bin/firstrun.sh /etc/my_runonce/firstrun.sh  
RUN chmod +x /etc/my_runonce/firstrun.sh  
  
# Add custom cron job during container startup  
ADD files/bin/startup.sh /etc/my_runalways/startup.sh  
ADD files/bin/grabber.sh /usr/local/bin/grabber  
RUN chmod +x /etc/my_runalways/startup.sh  
RUN chmod +x /usr/local/bin/grabber  

