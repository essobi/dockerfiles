#Rok4 build env  
FROM debian:wheezy  
MAINTAINER Thibault Coupin <thibault.coupin@ign.fr>  
  
#Get build env  
RUN apt-get update  
RUN apt-get install -y wget  
RUN apt-get install -y unzip  
RUN apt-get install -y build-essential gettext nasm automake cmake xsltproc  
RUN apt-get install -y perl libxml2-dev libgdal-perl liblog-log4perl-perl
libconfig-inifiles-perl libxml-libxml-simple-perl libfile-copy-link-perl  
  
#Add build script  
RUN mkdir /rok4-tobuild  
RUN chown 1000 /rok4-tobuild  
RUN chgrp 1000 /rok4-tobuild  
RUN chmod -R 777 /tmp  
USER 1000  
WORKDIR /rok4-tobuild  
ADD buildRok4.sh /buildRok4.sh  
CMD /bin/bash /buildRok4.sh  

