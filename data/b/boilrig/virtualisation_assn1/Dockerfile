##################  
# Data Container #  
##################  
  
# Linux Distro and Version  
FROM ubuntu:14.04  
  
# Dockerfile Maintainer  
MAINTAINER Matthew Chipping "boilrig@hotmail.com"  
  
# HTML Index  
ADD web /var/www/html/  
  
# Set Volume  
VOLUME [ "/var/www/html" ]  
  
# Entry Point Infinite Loop  
ENTRYPOINT [ "/bin/sh", "-c", "while true; do echo im a datacontainer mate;
sleep 60; done" ]  

