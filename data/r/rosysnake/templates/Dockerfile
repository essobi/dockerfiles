#base image to use as base layer (debian or busybox are smaller but may lack
some packages)  
FROM ubuntu:14.04  
  
#fill in the next line with all <package>.version you will install  
LABEL ubuntu.version="14.04"  
  
#uncomment the next line and add your name and institute (and email if wanted)
as author. you can also delete the next line and add maintainer="<your data>"
to the LABEL instruction  
#MAINTAINER  
  
USER root  
  
#which commands to run to build your image. Try if possible to leave only a
single RUN instruction to minimize the number of layers (just go to a new line
after && \\)  
RUN apt-get -y update && apt-get -yy install  
  
WORKDIR /data/  
  
#uncomment and fill in the next line if you want your image to run as
executable  
#ENTRYPOINT []  

