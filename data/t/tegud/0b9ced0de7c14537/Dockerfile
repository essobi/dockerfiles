FROM node:6.10.3  
ADD ./package.json /app/package.json  
ADD ./useragents.csv /app/useragents.csv  
ADD ./wdio.conf.js /app/wdio.conf.js  
ADD ./test /app/test  
  
WORKDIR /app  
  
RUN npm i  
  
ENTRYPOINT ["npm", "test"]  

