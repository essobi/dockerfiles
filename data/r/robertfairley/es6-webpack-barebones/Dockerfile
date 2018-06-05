#  
# ES6-WEBPACK-BAREBONES  
#  
FROM node:latest  
MAINTAINER Robert Fairley "rrafairley@gmail.com"  
# Process the app  
WORKDIR /tmp  
COPY package.json /tmp/  
COPY package-lock.json /tmp/  
RUN npm config set registry http://registry.npmjs.org  
RUN npm install  
  
WORKDIR /usr/var/app  
COPY . /usr/var/app  
RUN cp -a /tmp/node_modules /usr/var/app  
RUN npm run build  
  
# Expose the application port  
EXPOSE 1234  
# Start the static server  
CMD npm start  

