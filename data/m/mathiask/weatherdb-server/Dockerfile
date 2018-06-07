FROM node  
LABEL description="A simple node/express server connected to RethinkDB at host
rethinkdb"  
LABEL version="0.1"  
MAINTAINER Mathias Kegelmann  
  
WORKDIR /server  
  
COPY package.json .  
  
RUN npm install  
  
# copying the application after "npm install" to enable caching of node module
layers  
COPY src src  
  
ENTRYPOINT ["npm", "start"]  
  
EXPOSE 3000  

