FROM node:9  
WORKDIR /var/app  
  
COPY ./package.json /var/app/package.json  
RUN yarn install  
  
COPY . /var/app  
  
EXPOSE 8000  
ENTRYPOINT exec npm start  

