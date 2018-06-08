FROM debian:jessie  
  
RUN apt-get update  
ADD salt.list /etc/apt/sources.list.d/salt.list  
RUN apt-get install -y wget  
RUN wget -q -O- "http://debian.saltstack.com/debian-salt-team-
joehealy.gpg.key" | apt-key add -  
RUN apt-get update  
RUN apt-get install -y elvis-tiny kmod python-pip  
ENV DOCKER True  

