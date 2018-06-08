FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/doc  
  
WORKDIR /usr/src/doc  
  
RUN npm install -g https://github.com/marciocamurati/ramlo.git#v0.2.1.2  
  
CMD [ "ramlo", "-f", "api.raml" ]  

