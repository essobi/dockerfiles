FROM phusion/baseimage:0.9.18  
MAINTAINER https://github.com/uisge-beatha  
ENV DEBIAN_FRONTEND noninteractive  
  
######################################  
## Environment  
######################################  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
######################################  
# Set correct environment variables  
######################################  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
  
######################################  
## Configure Directories  
######################################  
## SickRage configuration folder  
VOLUME /Mylar-config  
  
## SickRage watched folder  
VOLUME /watched  
  
## Downloads  
VOLUME /downloads  
  
## media  
VOLUME /media  
  
## Default startup  
VOLUME /nonexistent  
  
######################################  
## Upgrade OS  
######################################  
RUN apt-get update -q && apt-get upgrade -y -o Dpkg::Options::="--force-
confold"  
######################################  
## Mylar setup  
######################################  
  
RUN apt-get install -qy python python-cherrypy git  
  
RUN git clone https://github.com/evilhero/mylar -b development /opt/Mylar  
  
  
  
######################################  
## Expose Ports  
######################################  
## Sonarr  
EXPOSE 8081  
######################################  
## Configure Service Accounts  
######################################  
######################################  
## Update Directory Permissions  
######################################  
######################################  
## Add Services to runit  
######################################  
## Add Mylar  
RUN mkdir /etc/service/Mylar  
ADD run.sh /etc/service/Mylar/run  
RUN chmod +x /etc/service/Mylar/run  
  
# Add 10_update_user.sh to execute during container startup  
ADD 10_update_user.sh /etc/my_init.d/10_update_user.sh  
RUN chmod +x /etc/my_init.d/10_update_user.sh  
  
  
  
  
  
######################################  
## Clean up APT when done.  
######################################  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

