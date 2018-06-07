FROM node  
  
RUN mkdir /app/  
  
WORKDIR /app/  
  
COPY package.json /app/  
  
COPY . /app/  
  
RUN rm -rf /app/node_modules/  
  
RUN npm install  
  
# COPY . /app/  
EXPOSE 3000  
CMD ["npm", "start"]  

