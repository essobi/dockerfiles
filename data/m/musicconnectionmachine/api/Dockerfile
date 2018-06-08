FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/api  
  
# Cache npm install  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN cp -a /tmp/node_modules /usr/src/api  
  
WORKDIR /usr/src/api  
  
# Install app dependencies  
COPY . /usr/src/api  
  
RUN npm run swagger-compile  
  
# Create the docs  
RUN cp api/swagger/swagger.json public/  
RUN sed -i 's/localhost:10010/mcmapi.azurewebsites.net/' public/swagger.json  
  
EXPOSE 10010  
CMD [ "npm", "start"]  

