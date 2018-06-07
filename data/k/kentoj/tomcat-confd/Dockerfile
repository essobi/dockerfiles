############################################################  
# Dockerfile to add in confd capability into tomcat  
# Based on tomcat library image  
############################################################  
  
FROM tomcat:8.0.23-jre8  
MAINTAINER Kent Johnson <kentoj@gmail.com>  
  
### INSTALL CONFD  
# Using only one run command to create only one additional layer for this
custom image  
RUN wget
https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-
amd64 && \  
mv confd-0.9.0-linux-amd64 /usr/local/bin/confd && \  
chmod +x /usr/local/bin/confd && \  
mkdir -p /etc/confd/conf.d /etc/confd/templates

