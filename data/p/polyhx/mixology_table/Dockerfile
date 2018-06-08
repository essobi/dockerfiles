FROM node:8.1.0-alpine  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/server  
RUN mkdir -p /usr/src/app/frontend  
WORKDIR /usr/src/app/server  
  
RUN mkdir -p /tmp/server  
RUN mkdir -p /tmp/frontend  
  
ADD frontend/package.json /tmp/frontend/package.json  
RUN cd /tmp/frontend && npm install  
RUN cp -a /tmp/frontend/node_modules /usr/src/app/frontend  
  
ADD server/package.json /tmp/server/package.json  
RUN cd /tmp/server && npm install  
RUN cp -a /tmp/server/node_modules /usr/src/app/server  
  
# Bundle app source  
ADD . /usr/src/app  
  
RUN cd /usr/src/app/frontend && npm run build  
RUN npm run build  
  
EXPOSE 8189  
CMD [ "npm", "start" ]  

