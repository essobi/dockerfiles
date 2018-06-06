FROM node:8  
  
WORKDIR /home/node  
COPY . /home/node  
RUN npm install  
  
USER node  
EXPOSE 5000  
  
CMD [ "npm", "start" ]  
  

