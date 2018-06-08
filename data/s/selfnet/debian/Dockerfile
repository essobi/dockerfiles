FROM debian:jessie  
MAINTAINER Selfnet e.V Ops Monkeys  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://mirror.selfnet.de/apt-mirror/debian.saltstack.com/debian
jessie-saltstack main" > /etc/apt/sources.list.d/salt.list  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget  
RUN wget -q -O - "http://mirror.selfnet.de/apt-
mirror/debian.saltstack.com/debian-salt-team-joehealy.gpg.key" | apt-key add -  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
git \  
rsyslog \  
salt-minion \  
python-dateutil \  
python-redis  

