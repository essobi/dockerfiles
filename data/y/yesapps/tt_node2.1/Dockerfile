FROM node:latest  
  
MAINTAINER Kishore Chandra - kishorechandra.developer@gmail.com  
  
ENV NODE_ENV=production  
ENV PORT=8022  
COPY . /var/www  
WORKDIR /var/www  
  
VOLUME ["/var/www"]  
  
RUN ["npm", "install"]  
  
EXPOSE $PORT  
  
ENTRYPOINT ["npm", "start"]  

