FROM node:7.5  
RUN npm install -g yarn  
  
COPY ./ /root/app/  
  
WORKDIR /root/app/  
  
RUN yarn install  
  
EXPOSE 8080  
CMD node index.js  

