FROM node:7.0.0  
MAINTAINER pascal.gremaud@unifr.ch  
  
ENV appdir /usr/src/app/  
  
RUN mkdir -p $appdir  
  
WORKDIR $appdir  
  
COPY package.json .  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 8080  
CMD ["node", "."]  

