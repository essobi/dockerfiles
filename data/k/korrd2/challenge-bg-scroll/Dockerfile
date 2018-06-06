FROM node:alpine  
RUN mkdir -p /app  
WORKDIR /app  
  
# Install dependencies  
COPY package.json /app/  
RUN npm install  
  
COPY . /app  
  
EXPOSE 3000  
ENTRYPOINT ["npm", "start"]  

