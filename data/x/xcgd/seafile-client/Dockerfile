FROM phusion/baseimage:0.9.20  
MAINTAINER release@xcg-consulting.fr  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
software-properties-common  
RUN apt-add-repository ppa:seafile/seafile-client  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install seafile-cli  
  
RUN mkdir /etc/service/ccnet  
COPY ccnet.sh /etc/service/ccnet/run  
RUN chmod +x /etc/service/ccnet/run  
RUN mkdir /etc/service/seafiled  
COPY seafiled.sh /etc/service/seafiled/run  
RUN chmod +x /etc/service/seafiled/run  

