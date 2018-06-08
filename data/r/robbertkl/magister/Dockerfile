FROM robbertkl/node:latest  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
COPY package.json ./  
RUN npm install  
COPY . .  
  
ENTRYPOINT [ "node", "app" ]  
CMD []  

