FROM node  
RUN mkdir -p /app  
COPY . /app  
WORKDIR /app  
COPY package.json /app  
RUN npm install  
  
EXPOSE 80  
CMD npm start  

