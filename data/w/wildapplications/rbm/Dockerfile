FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
# Install app dependencies  
COPY package.json /usr/app  
RUN npm install  
  
COPY server.js /usr/app  
  
#COPY .angular-cli.json /usr/app  
# Bundle app source  
# ADD src /usr/app/src  
# UNCOMMENT FOR DIST  
# Bundle app distribution  
ADD dist /usr/app/dist  
  
EXPOSE 8080  
# dev  
#CMD [ "npm" , "run-script","build" ]  
# DIST  
CMD [ "npm", "start" ]  

