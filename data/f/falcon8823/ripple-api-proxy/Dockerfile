FROM node:6.2.1  
ENV APP_HOME /usr/local/ripple-api-proxy  
  
WORKDIR $APP_HOME  
COPY package.json package.json  
RUN npm install  
  
COPY . $APP_HOME  
WORKDIR $APP_HOME  
  
EXPOSE 40000  
CMD ["node", "rap.js"]  

