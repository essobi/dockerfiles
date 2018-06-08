# Generic salts masterless minion  
# Base image  
FROM ubuntu:latest  
  
MAINTAINER Erik Kaareng-Sunde esu@enonic.com  
  
  
  
  
  
# Set timezone to Europe/Oslo  
ADD configs/timezone /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Installing saltstack  
RUN apt-get update  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository ppa:saltstack/salt  
RUN apt-get update  
RUN apt-get -y install salt-minion python-apt  
ADD configs/minion /etc/minion  
  
EXPOSE 8080  
CMD /bin/bash  

