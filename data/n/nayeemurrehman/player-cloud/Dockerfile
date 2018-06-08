FROM node:8.9.1  
ENV NODE_ENV production  
WORKDIR /app  
COPY package.json /app  
RUN npm install  
COPY . /app  
CMD npm start  

