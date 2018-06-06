FROM node  
  
CMD mkdir -p /app  
WORKDIR /app  
COPY . /app  
COPY /code/package.json /app  
RUN npm install  
  
EXPOSE 3000  
CMD cd /app/code && npm start  

