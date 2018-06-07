# GrooveBasin image  
# use the ubuntu base image provided by dotCloud  
FROM ubuntu:precise  
  
MAINTAINER Simon Morvan garphy@zone84.net  
  
# /sbin/initctl hack  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN rm /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
# Install apt-add-repositor  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-
properties  
  
# Add some PPAs  
RUN apt-add-repository ppa:andrewrk/libgroove  
RUN apt-add-repository ppa:chris-lea/node.js  
RUN apt-get update  
  
# Install build & core tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential git vim-
tiny  
  
# Install libgroove  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libgroove-dev
libgrooveplayer-dev libgrooveloudness-dev libgroovefingerprinter-dev  
  
# Install node.js  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs  
  
# Install python easy_install  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-pip python-
setuptools  
  
# Install supervisor  
RUN easy_install supervisor  
  
RUN mkdir /home/groovebasin && cd /home/groovebasin && git clone
https://github.com/andrewrk/groovebasin.git  
RUN cd /home/groovebasin/groovebasin && npm run build  
  
ADD ./start.sh /start.sh  
ADD ./foreground.sh /home/groovebasin/foreground.sh  
ADD ./supervisord.conf /etc/supervisord.conf  
  
RUN chmod 755 /start.sh /home/groovebasin/foreground.sh  
  
EXPOSE 16242  
EXPOSE 6600  
VOLUME /music  
CMD ["/bin/bash", "/start.sh"]  

