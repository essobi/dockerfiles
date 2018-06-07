# Hastebin on Docker  
# VERSION 0.1  
FROM dockerfile/nodejs  
MAINTAINER John Vrbanac <john.vrbanac@linux.com>  
  
RUN git clone https://github.com/seejohnrun/haste-server.git /opt/haste  
WORKDIR /opt/haste  
RUN npm install  
  
ADD config.js /opt/haste/config.js  
  
EXPOSE 7777  
CMD ["npm", "start"]

