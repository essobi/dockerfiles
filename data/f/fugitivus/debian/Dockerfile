#debian container for general purpose:  
FROM debian:latest  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
#install updates, some packages and do cleanup:  
RUN apt-get update && apt-get upgrade -y\  
&& apt-get install apt-utils -y\  
&& apt-get install net-tools aptitude -y\  
&& apt-get clean autoclean\  
&& apt-get autoremove -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  

