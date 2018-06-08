FROM node:6  
MAINTAINER Oles Savluk <savluk.oles@gmail.com>  
  
RUN mkdir /app  
WORKDIR /app  
  
ADD . .  
COPY ./.env.sample ./.env  
  
RUN npm set progress=false && \  
npm install -g --progress=false yarn  
  
RUN yarn  
  
VOLUME /app/public  
  
EXPOSE 8080  
CMD node server.js  

