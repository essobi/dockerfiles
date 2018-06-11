FROM python:3  
  
MAINTAINER Aleksi Häkli <aleksi.hakli@vincit.fi>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update \  
&& apt-get -qy dist-upgrade  
  
RUN useradd -d /home/jenkins -m -u 1000 jenkins  
  

