FROM node:latest  
  
MAINTAINER Jopy Henriques (jopy.c.henriques@accenture.com)  
  
# add the files to load  
ADD ./ .  
  
# Change permission to wait-for-it.sh  
RUN chmod 755 wait-for-it.sh  
  
# install all needed packages  
RUN npm install  
  
# expose port  
EXPOSE 80  
# execute server.js  
ENTRYPOINT ["node", "server.js"]  

