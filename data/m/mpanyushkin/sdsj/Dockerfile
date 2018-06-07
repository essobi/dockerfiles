FROM node:5.4.0  
MAINTAINER misha.panyushkin@gmail.com  
  
# Using cached layers for modules  
WORKDIR /tmp  
ADD package.json /tmp/package.json  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install  
RUN mkdir -p /usr/src/app  
RUN cp -a /tmp/node_modules /usr/src/app  
  
RUN npm install -g nodemon  
  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app  
  
EXPOSE 8080  
CMD [ "npm", "run", "prod" ]

