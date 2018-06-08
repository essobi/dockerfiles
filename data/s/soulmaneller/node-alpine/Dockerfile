FROM alpine  
MAINTAINER oxoox22@gmail.com <Oxoox Soulmaneller>  
  
RUN apk add --update nodejs  
RUN npm i -g forever  
RUN npm i -g supervisor  
RUN npm i -g nodemon  
  
EXPOSE 3000  
WORKDIR /app  
# CMD forever forever/forever.json  
CMD node index.js  

