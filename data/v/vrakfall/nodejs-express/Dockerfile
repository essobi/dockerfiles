FROM node:latest  
MAINTAINER Vrakfall <jeremy@artphotolaurent.be>  
  
RUN npm install express serve-favicon config morgan async node-minify \  
handlebars lodash walk pm2  
  
VOLUME ["/usr/src/app"]  
  
EXPOSE 4000  
WORKDIR /usr/src/app  
  
CMD ["node", "app.js"]  

