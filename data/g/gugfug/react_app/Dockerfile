FROM node:latest  
  
WORKDIR /usr/www  
  
COPY ./package.json .  
RUN npm install --silent  
  
EXPOSE 80  
COPY ./gulpfile.js .  
COPY ./webpack_config ./webpack_config  
  
ENTRYPOINT [ "npm", "run" ]  
CMD [ "serve" ]  

