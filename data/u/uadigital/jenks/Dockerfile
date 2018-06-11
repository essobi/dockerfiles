FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/jenks  
WORKDIR /usr/src/jenks  
  
COPY package.json /usr/src/jenks/  
RUN npm install  
RUN npm build  
COPY . /usr/src/jenks  
  
EXPOSE 3000  
#RUN npm run browsersync  

