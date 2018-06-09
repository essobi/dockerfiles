FROM node:latest  
  
MAINTAINER Tim Brandin "tim.brandin@studiointeract.se"  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
RUN apt-get install --no-install-recommends -y -q sudo curl python build-
essential git ca-certificates  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen &&
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && dpkg-reconfigure
--frontend=noninteractive locales && update-locale LANG=en_US.UTF-8  
RUN export LANG=en_US.UTF-8  
  
RUN adduser --disabled-password --gecos '' builder  
RUN usermod -aG sudo builder  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Fixes issues with builds not going through on Bitbucket Pipeline due to  
# issues reaching unicode.org.  
RUN apt-get install unicode-data  
  
USER builder  

