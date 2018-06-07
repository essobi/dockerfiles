FROM gutenye/node  
  
COPY . /app  
  
WORKDIR /app/client  
RUN bower install --allow-root  
  
WORKDIR /app/server  
RUN yarn --prod  
  
EXPOSE 80  
  
CMD [ "npm", "start" ]  

