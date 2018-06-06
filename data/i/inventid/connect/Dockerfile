FROM node:latest  
MAINTAINER Rogier Slag  
  
# Make the machine up to date and install some dependencies  
RUN apt-get update && \  
apt-get install -y git curl && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Export the database, originals dir and the config dir  
RUN mkdir /opt/connect  
RUN mkdir /opt/connect/config  
RUN mkdir /opt/connect/assets  
  
VOLUME ["/opt/connect/config"]  
EXPOSE 8080  
# Install bower  
RUN npm install -g bower pm2  
  
# Add the dependencies  
ADD package.json /opt/connect/package.json  
RUN cd /opt/connect && npm install  
  
# Add bower stuff  
ADD assets/bower.json /opt/connect/assets/  
RUN cd /opt/connect/assets && bower install --allow-root  
  
# Add the application  
ADD assets/*.html /opt/connect/assets/  
ADD assets/style.css /opt/connect/assets/  
ADD assets/js /opt/connect/assets/js  
  
ADD server.js /opt/connect/server.js  
  
# Run the entire thing!  
WORKDIR /opt/connect  
CMD ["/usr/local/bin/pm2", "start", "server.js", "--no-daemon","--
instances=0"]  

