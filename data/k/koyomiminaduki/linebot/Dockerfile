FROM node:6.3.1-slim  
ENV APP_ROOT /usr/src/base-express  
  
WORKDIR $APP_ROOT  
COPY package.json $APP_ROOT  
COPY npm-shrinkwrap.json $APP_ROOT  
RUN npm install && npm cache clean  
  
COPY . $APP_ROOT  
EXPOSE 3000  
CMD ["npm", "start"]  
  

