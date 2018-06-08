FROM ubuntu:14.10  
MAINTAINER Romain Commandé, commande.romain@gmail.com  
  
RUN mkdir /data  
RUN mkdir /zeo/  
RUN apt-get update  
RUN apt-get install -y python3-pip python3-dev  
RUN pip3 install ZEO  
ADD zeo.conf /srv/zeo.conf  
CMD runzeo -C /srv/zeo.conf  
VOLUME /zeo/  
VOLUME /data/packages  

