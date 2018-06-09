# Version: -1.0.1  
#Ubuntu 13.04 image  
FROM ubuntu:14.04  
#Set Maintainer  
MAINTAINER Matthew Taylor "taylomj5@student.op.ac.nz"  
#updates and installs  
RUN apt-get update && apt-get -y dist-upgrade  
RUN apt-get -y upgrade  
RUN apt-get -y install  
RUN apt-get -y install openssh-server  
RUN apt-get -y install supervisor  
  
#Copy supervisor to /etc/supervisor...  
COPY supervisord.conf /etc/supervisor/conf.d/supervisor.conf  
COPY foo /etc/foo  
  
#Expose Ports  
EXPOSE 22 80  
  
#Run command  
CMD ["/usr/bin/supervisord"]  

