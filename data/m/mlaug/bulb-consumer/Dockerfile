FROM node:7.9.0  
COPY package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /usr/app && cp -a /tmp/node_modules /usr/app  
  
COPY ./ /usr/app/  
RUN cd /usr/app && npm test  
WORKDIR /usr/app  
  
CMD ["npm", "run", "consumer"]

