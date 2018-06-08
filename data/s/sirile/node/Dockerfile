# Create a docker base image for nodejs, git and a few essentials  
FROM sirile/ubuntu:0.9  
MAINTAINER Ilkka Anttonen version: 0.9  
# Install node, npm  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12  
RUN echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu $(lsb_release
-cs) main" > /etc/apt/sources.list.d/node.list  
RUN apt-get update  
RUN apt-get -y install nodejs  

