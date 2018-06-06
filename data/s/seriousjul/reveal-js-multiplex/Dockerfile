FROM node:6-alpine  
  
# Get multiplex deps  
RUN mkdir -p /tmp  
RUN mkdir -p /usr/src  
WORKDIR /tmp  
COPY package.json /tmp  
RUN npm install \  
&& mv node_modules/reveal.js/plugin/multiplex /usr/src/app \  
&& rm -rf /tmp  
  
# Install app dependencies  
WORKDIR /usr/src/app  
RUN npm install  
  
ENV PORT 80  
EXPOSE 80  
CMD [ "npm", "start" ]

