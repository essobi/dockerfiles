FROM node:4.2.1  
ENV APP_HOME /app  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
COPY package.json $APP_HOME  
RUN npm install --production && npm install supervisor -g  
COPY . $APP_HOME  
EXPOSE 5000  
CMD ["npm", "start"]

