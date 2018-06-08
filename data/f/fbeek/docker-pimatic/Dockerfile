############################################################  
# Dockerfile to build Pimatic container images  
# Based on Debian  
############################################################  
  
# Set the base image to Ubuntu  
FROM debian  
  
# File Author / Maintainer  
MAINTAINER SLiX  
  
################## BEGIN INSTALLATION ######################  
# Install NodeJS v0.10.41  
RUN apt-get update  
RUN apt-get --yes install curl build-essential apt-utils git dialog wget  
RUN curl -sL https://deb.nodesource.com/setup_0.10 | bash -  
RUN apt-get install --yes nodejs  
  
# Install Pimatic Following the Instructions at Pimatic Docs  
# Ref: https://pimatic.org/guide/getting-started/installation/  
RUN mkdir /home/pimatic/  
RUN mkdir /home/pimatic/pimatic-app && touch /home/pimatic/pimatic-
app/.npmignore  
RUN cd /home/pimatic/ && npm install pimatic --prefix pimatic-app --production  
RUN cp /home/pimatic/pimatic-app/node_modules/pimatic/config_default.json
/home/pimatic/pimatic-app/config.json  
RUN cd /home/pimatic/pimatic-app/node_modules/pimatic && npm link && wget
https://raw.github.com/pimatic/pimatic/master/install/pimatic-init-d && cp
pimatic-init-d /etc/init.d/pimatic  
RUN chmod +x /etc/init.d/pimatic  
RUN chown root:root /etc/init.d/pimatic  
RUN update-rc.d pimatic defaults  
RUN sed -i "s/\"password\": \"\"/\"password\": \"abcd1234\"/g"
/home/pimatic/pimatic-app/config.json  
  
  
# Expose port 80  
EXPOSE 80  

