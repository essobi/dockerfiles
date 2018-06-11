#  
# Node.js Dockerfile # https://github.com/dockerfile/nodejs  
# Source: https://github.com/nickjanssen/docker-nodebb/blob/master/Dockerfile  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Install Node.js  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install nodejs-legacy -y  
RUN apt-get install npm -y  
RUN cd /opt && git clone https://github.com/NodeBB/NodeBB.git nodebb  
RUN cd /opt/nodebb && npm install  
RUN apt-get install imagemagick -y  
  
RUN cd /opt/nodebb && npm install redis && npm install connect-redis  
  
VOLUME /opt/nodebb  
  
# Define working directory.  
WORKDIR /opt/nodebb  
EXPOSE 4567  
# Define default command.  
CMD ["node", "app.js"]

