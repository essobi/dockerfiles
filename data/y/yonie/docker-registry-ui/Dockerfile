FROM yonie/nodejs  
  
MAINTAINER yonie (yong_cyril@163.com)  
  
ADD public /app/public  
ADD server /app/server  
  
WORKDIR /app/server  
RUN npm install  
  
CMD node app.js

