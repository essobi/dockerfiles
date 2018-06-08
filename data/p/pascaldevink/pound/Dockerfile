FROM phusion/baseimage  
MAINTAINER Pascal de Vink <pascal.de.vink@gmail.com>  
  
RUN apt-get update && apt-get install -y pound  
RUN sed -i 's/startup\=0/startup\=1/' /etc/default/pound  
  
RUN mkdir -p /etc/my_init.d  
ADD pound.sh /etc/my_init.d/pound.sh  
  
CMD ["/sbin/my_init"]  

