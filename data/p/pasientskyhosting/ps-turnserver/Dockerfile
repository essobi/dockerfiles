FROM phusion/baseimage  
MAINTAINER Joakim Karlsson <jk@patientsky.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get update -y  
RUN apt-get install coturn net-tools -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /etc/service/turnserver  
  
ADD turnserver.sh /etc/service/turnserver/run  
ADD turnserver.conf /etc/turnserver.conf  
  
RUN chmod +x /etc/service/turnserver/run  
  
EXPOSE 3478/udp  
EXPOSE 49152-65000/udp  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

