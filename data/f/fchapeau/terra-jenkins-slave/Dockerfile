FROM jenkinsci/jnlp-slave  
MAINTAINER Francois Drouin-Morin  
USER root  
  
RUN apt-get update  
RUN apt-get install chromium wget xvfb x11-xkb-utils xfonts-100dpi
xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps git sudo -y  
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  

