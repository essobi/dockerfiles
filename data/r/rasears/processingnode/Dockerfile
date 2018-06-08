FROM node:carbon  
  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm install  
  
COPY . .  
  
COPY sample_product_data.tsv ./sample_product_data.tsv  
  
EXPOSE 8088  
CMD [ "npm", "start" ]

