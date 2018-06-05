FROM node:8.1  
WORKDIR /src  
COPY ./lib ./lib  
ADD ./index.js ./index.js  
ADD ./package.json ./package.json  
ADD ./package-lock.json ./package-lock.json  
  
RUN npm install --production  
  
CMD ["npm", "start"]  

