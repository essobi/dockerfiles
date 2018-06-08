FROM node:8.9.1  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
# install packages  
RUN npm install  
  
# copy source files  
COPY . .  
  
# build the React app with ES6 to ES5 Javascript  
RUN npm run build  
  
EXPOSE 5000  
CMD [ "npm", "start" ]  

