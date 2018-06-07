FROM node:0.12.7  
MAINTAINER Rogier Slag  
  
# Make the machine up to date and install some dependencies  
RUN apt-get update && \  
apt-get install -y git curl && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Export the database, originals dir and the config dir  
RUN mkdir /opt/zoopeeker  
  
EXPOSE 8080  
# Install bower  
RUN npm install -g bower  
  
# Add the dependencies  
ADD . /opt/zoopeeker  
RUN cd /opt/zoopeeker && npm install && bower install --allow-root  
  
# Run the entire thing!  
WORKDIR /opt/zoopeeker  
CMD ["node", "app.js"]  
  

