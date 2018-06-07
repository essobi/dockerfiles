FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY . /usr/src/app  
  
ENV NODE_ENV production  
ENV NPM_CONFIG_PRODUCTION false  
  
RUN npm install  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

