FROM node:7.2.1  
MAINTAINER pokemon-yellow  
  
ENV appdir /usr/src/app/  
  
RUN mkdir -p $appdir  
  
WORKDIR $appdir  
  
COPY package.json .  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 5000  
CMD ["node", "."]

