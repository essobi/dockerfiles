FROM node:latest  
  
MAINTAINER xsota  
  
  
VOLUME ["/md", "/public"]  
  
ADD gulpfile.js /gulpfile.js  
  
RUN npm install -g gulp\  
&& npm install gulp gulp-watch gulp-aglio gulp-plumber  
  
CMD gulp watch  

