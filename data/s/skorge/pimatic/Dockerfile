##################################################################  
# Dockerfile to create a PIMATIC container  
# Tested and designed for Synology Diskstation but should run in all docker
environments.  
##################################################################  
  
# We are using nodeJS as the base image  
FROM node:4  
  
# Author  
MAINTAINER skorge  
  
####### PIMATIC installaton #######  
RUN mkdir /home/pimatic-app  
RUN /usr/bin/env node --version  
RUN cd /home && npm install pimatic --prefix pimatic-app --production  
  
  
####### Instal globally #######  
RUN cd /home/pimatic-app/node_modules/pimatic && npm link  
  
####### Copy the default config to our installation #######  
COPY config_default.json /home/pimatic-app/config.json  
RUN touch /home/pimatic-app/pimatic-daemon.log  
  
####### Start the pimatic service #######  
ENTRYPOINT cd /home/pimatic-app && pimatic.js start && tail -f pimatic-
daemon.log  
  
# Expose pimatic port e.g. 80  
EXPOSE 80  

