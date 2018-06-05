###########################################################  
# Image that runs a status collection service for scrapers.  
# Receives link from a MongoDB container and links to the  
# hdx-monitor-server.  
###########################################################  
  
FROM node:latest  
  
MAINTAINER Luis Capelo <luiscape@gmail.com>  
  
RUN \  
npm install -g pm2 \  
&& git clone http://github.com/rolltime/rolltime-node-watch \  
&& cd rolltime-node-watch \  
npm install  
  
#  
# Install the MongoDB shell  
# for configuring the database.  
#  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.0.list \  
&& apt-get update \  
&& apt-get install -y mongodb-org-shell  
  
  
WORKDIR '/rolltime-node-watch'  
  
EXPOSE 9000  
  
CMD ["make", "run"]  

