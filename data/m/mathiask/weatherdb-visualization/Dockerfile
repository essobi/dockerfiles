FROM node  
LABEL description="A simple node app serving a p5js web page"  
LABEL version="0.1"  
MAINTAINER Mathias Kegelmann  
  
WORKDIR /app  
  
COPY package.json .  
  
RUN npm install  
  
# copying the application after "npm install" to enable caching of node module
layers  
COPY . .  
  
ENTRYPOINT ["npm", "start"]  
  
EXPOSE 80  

