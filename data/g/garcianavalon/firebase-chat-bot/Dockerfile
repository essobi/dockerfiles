FROM node:7.2.0  
MAINTAINER Enrique Garcia Navalon "garcianavalon@gmail.com"  
RUN mkdir -p /app  
WORKDIR /app  
EXPOSE 3000  
CMD ["npm", "start"]  
  
# nodemon for live reloading in development  
RUN npm install -gq nodemon  
  
COPY ./package.json .  
RUN npm install -q  
  
COPY ./ .  

