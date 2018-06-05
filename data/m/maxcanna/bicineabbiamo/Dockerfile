FROM node:alpine  
MAINTAINER Massimiliano Cannarozzo <maxcanna@gmail.com>  
  
EXPOSE 3000  
ADD ./ /var/www/bicineabbiamo/  
RUN cd /var/www/bicineabbiamo/ && npm i --production  
  
WORKDIR /var/www/bicineabbiamo  
  
CMD ["node", "index.js"]  

