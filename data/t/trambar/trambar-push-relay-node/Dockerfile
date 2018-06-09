FROM node:6  
WORKDIR /opt/trambar-push-relay  
  
# install dependencies  
COPY package.json ./  
RUN npm install  
  
# copy codebase  
COPY src src/  
  
WORKDIR /opt/trambar-push-relay/src  

