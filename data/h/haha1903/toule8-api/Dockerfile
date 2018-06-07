FROM node:latest  
MAINTAINER changhai  
  
# 80 = HTTP, 443 = HTTPS, 3000 = MEAN.JS server, 35729 = livereload  
EXPOSE 80 443 3000 35729  
# Install MEAN.JS Prerequisites  
WORKDIR /opt/express  
  
COPY . /opt/express  
  
RUN npm install  
  
# Run MEAN.JS server  
CMD ["node","app.js"]  
  

