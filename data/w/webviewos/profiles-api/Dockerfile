FROM node:7.2.0  
ENV NODE_ENV production  
ENV APP_DIR /app  
  
RUN mkdir $APP_DIR  
  
ADD . $APP_DIR  
  
WORKDIR $APP_DIR  
  
RUN npm install -g babel-cli  
RUN npm install  
  
ENTRYPOINT ["babel-node", "app.js"]  

