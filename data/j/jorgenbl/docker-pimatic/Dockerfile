##################################################################  
# pimatic docker file  
# VERSION 0.1  
##################################################################  
  
# base image  
FROM node:4-slim  
  
LABEL Description="Pimatic docker image"  
  
RUN apt-get update \  
&& apt-get install -y \  
git build-essential make python python-pip avahi-daemon avahi-discover libnss-
mdns libavahi-compat-libdnssd-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
####### enable dbus (for pimatic-hap) #######  
RUN sed -i -- 's/#enable-dbus=yes/enable-dbus=yes/g' /etc/avahi/avahi-
daemon.conf  
  
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
RUN cp /opt/pimatic-docker/node_modules/pimatic/config_default.json
/data/config.json  
RUN sed -i "s/\"password\": \"\"/\"password\": \"pimatic\"/g"
/data/config.json  
RUN sed -i "s/\"port\": 80\"\"/\"port\": 8086/g" /data/config.json  
  
RUN touch /data/pimatic-database.sqlite  
  
#RUN npm install node-gyp  
  
####### default plugins #######  
RUN cd /opt/pimatic-docker/ \  
&& npm install pimatic-cron \  
&& npm install pimatic-mobile-frontend \  
&& npm install pimatic-hap \  
&& cd node_modules/pimatic-hap \  
&& npm install \  
&& cd node_modules/hap-nodejs \  
&& npm install \  
&& cd /opt/pimatic-docker/ \  
&& npm install pimatic-shell-execute \  
&& npm install pimatic-log-reader \  
&& npm install pimatic-angular-material-frontend  
  
####### volume #######  
VOLUME ["/data"]  
  
####### command #######  
CMD ln -fs /data/config.json /opt/pimatic-docker/config.json && \  
ln -fs /data/pimatic-database.sqlite /opt/pimatic-docker/pimatic-
database.sqlite && \  
/etc/init.d/dbus restart && \  
avahi-daemon -D && \  
pimatic.js  
  
  
####### port #######  
EXPOSE 8086  

