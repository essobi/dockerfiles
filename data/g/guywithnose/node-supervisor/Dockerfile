FROM node  
  
VOLUME /nodeapp  
WORKDIR /nodeapp  
  
RUN npm install supervisor -g  
  
EXPOSE 9000  
CMD supervisor index.js  

