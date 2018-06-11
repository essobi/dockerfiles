# https://github.com/nimmis/docker-ubuntu  
FROM ubuntu:17.10  
MAINTAINER Stefan Schatz <stefan.schatz@osbg.at>  
  
# disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV TERM xterm  
  
# Do OS fixes  
COPY prepareUbuntu.sh /root/prepareUbuntu.sh  
RUN /root/prepareUbuntu.sh && rm -f /root/prepareUbuntu.sh  
  
# configure supervisor  
COPY supervisor/ /etc/supervisor/  
  
# Add my_init script and help scripts  
COPY bin/ /sbin/  
  
# add runonce and runalways scripts  
COPY my_runonce/ /etc/my_runonce/  
COPY my_runalways/ /etc/my_runalways/  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["/sbin/my_init"]  
  

