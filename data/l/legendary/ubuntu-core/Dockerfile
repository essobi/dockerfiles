FROM ubuntu:16.04  
MAINTAINER Legendary Hosting <mail@legendary-server.de>  
  
# Keep upstart from complaining  
RUN dpkg-divert --local --rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
RUN mkdir /var/run/sshd  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Basic Requirements  
RUN apt-get -y install pwgen python-setuptools curl git nano vim sudo unzip
openssh-server openssl  
  
# clean up unneeded packages  
RUN apt-get \--purge autoremove -y  
  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Initialization and Startup Script  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
#NETWORK PORTS  
# private expose  
EXPOSE 22  
  
# volume for mysql database and wordpress install  
#VOLUME ["/var/run/sshd"]  
  
CMD ["/bin/bash", "/start.sh"]  

