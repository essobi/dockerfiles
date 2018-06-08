FROM ubuntu:16.04  
MAINTAINER obed.n.munoz@gmail.com  
  
# Update and set OpenStack (Pike) ackages repository  
RUN apt-get update -y  
RUN apt install software-properties-common -y  
RUN add-apt-repository cloud-archive:pike -y  
RUN apt-get update -y  
  
# OpenStack Client  
RUN apt install python-openstackclient -y  
  
# Keystone and Apache2  
RUN apt install keystone apache2 libapache2-mod-wsgi -y  
  
# Keystone Configuration  
RUN mkdir -p /etc/keystone  
COPY keystone.conf /etc/keystone  
COPY bootstrap.sh /usr/bin/bootstrap.sh  
COPY openrc /root/openrc  
  
CMD ["/usr/bin/bootstrap.sh"]

