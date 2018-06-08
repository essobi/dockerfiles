##################################################################  
# pimatic docker file  
# VERSION 0.1  
##################################################################  
  
# base image  
FROM node:4  
  
LABEL Description="Pimatic docker image" Maintainer="trebankosta@gmail.com"
Version="0.1"  
  
####### install #######  
RUN mkdir /opt/pimatic-docker  
RUN cd /opt && npm install pimatic --prefix pimatic-docker --production  
RUN cd /opt/pimatic-docker/node_modules/pimatic && npm link  
  
####### autostart #######  
RUN wget
https://raw.githubusercontent.com/pimatic/pimatic/v0.9.x/install/pimatic-
init-d && cp pimatic-init-d /etc/init.d/pimatic  
RUN chmod +x /etc/init.d/pimatic  
RUN chown root:root /etc/init.d/pimatic  
RUN update-rc.d pimatic defaults  
  
####### init #######  
RUN mkdir /data/  
COPY ./config.json /data/config.json  
  
RUN touch /data/pimatic-database.sqlite  
  
####### default plugins #######  
RUN cd /opt/pimatic-docker/ \  
&& npm install pimatic-cron \  
&& npm install pimatic-mobile-frontend  
  
####### volume #######  
VOLUME ["/data"]  
  
####### command #######  
CMD ln -fs /data/config.json /opt/pimatic-docker/config.json && \  
ln -fs /data/pimatic-database.sqlite /opt/pimatic-docker/pimatic-
database.sqlite && \  
pimatic.js  
  

