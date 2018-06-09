FROM node:4-onbuild  
EXPOSE 8888  
WORKDIR /app  
ADD . /app  
  
RUN npm i  
  
ENV NAME Test  
  
cmd ["node", "app.js"]  

