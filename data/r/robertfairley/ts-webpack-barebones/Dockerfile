#  
# TS-WEBPACK-BAREBONES DOCKERFILE  
#  
FROM node:latest  
MAINTAINER Robert Fairley "rrafairley@gmail.com"  
# Process the app  
WORKDIR /tmp  
COPY package.json /tmp/  
COPY package-lock.json /tmp/  
RUN npm config set registry http://registry.npmjs.org  
RUN npm install -g typescript  
RUN npm install  
  
WORKDIR /usr/var/app  
COPY . /usr/var/app  
RUN cp -a /tmp/node_modules /usr/var/app  
RUN rm -rf /tmp/node_modules /tmp/package.json /tmp/package-lock.json  
RUN npm run build  
  
# Expose the dev port  
EXPOSE 1234  
# Start the dev server  
CMD ["npm", "start"]  
  

