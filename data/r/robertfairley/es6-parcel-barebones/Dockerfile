#  
# ES6-PARCEL-BAREBONES DOCKERFILE  
#  
FROM node:latest  
MAINTAINER Robert Fairley "rrafairley@gmail.com"  
# Process the app  
WORKDIR /tmp  
COPY package.json /tmp/  
RUN npm config set registry http://registry.npmjs.org  
RUN npm install -g parcel-bundler  
RUN npm install  
  
WORKDIR /var/www  
COPY . /var/www  
RUN cp -a /tmp/node_modules /var/www  
RUN npm run build  
  
# Expose the server port  
EXPOSE 1234  
# Run the app  
CMD npm start  
  

