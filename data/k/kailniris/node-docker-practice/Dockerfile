FROM node:8.1.3  
WORKDIR /app  
  
ADD ./src /app/src  
  
COPY package.json /app  
RUN npm install  
  
EXPOSE 3000  
CMD [ "npm", "start" ]

