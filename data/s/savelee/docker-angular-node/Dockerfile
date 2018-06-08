FROM node:latest  
MAINTAINER Lee Boonstra <leeboonstra@google.com>  
  
# Set in what directory commands will run  
WORKDIR /home/app  
  
# Put all our code inside that directory that lives in the container  
ADD . /home/app  
  
# Install dependencies  
RUN npm install  
  
# Tell Docker we are going to use this port  
EXPOSE 9000  
# run application  
# The command to run our app when the container is run  
CMD ["node", "server/app.js"]  

