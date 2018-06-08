FROM node:wheezy  
COPY . /blog/  
WORKDIR /blog  
  
RUN yarn install  
  
EXPOSE 3000  
CMD ["node", "index.js"]  

