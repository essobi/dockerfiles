FROM node:6.9.4  
MAINTAINER misha.panyushkin@gmail.com  
  
# Using cached layers for modules  
WORKDIR /tmp  
ADD package.json /tmp/package.json  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install  
RUN mkdir -p /usr/src/app  
RUN cp -a /tmp/node_modules /usr/src/app  
  
RUN npm install -g nodemon  
RUN npm install -g pm2  
  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app  
  
EXPOSE 8080  
CMD [ "npm", "run", "prod" ]

