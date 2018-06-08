FROM debian:jessie  
MAINTAINER Gediminas Ubartas <gediminas@cornercasetech.com>  
  
RUN apt-get update  
RUN apt-get --assume-yes install apt-transport-https ca-certificates curl
gnupg2 software-properties-common  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable"  
RUN apt-get update  
RUN apt-get --assume-yes install docker-ce  
RUN curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose

