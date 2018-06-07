FROM node:9-alpine  
  
COPY . /code  
RUN chown -R node. /code  
  
USER node  
WORKDIR /code  
EXPOSE 3000  
RUN npm install  
  
CMD npm start  

