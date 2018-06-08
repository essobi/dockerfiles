FROM node:8  
WORKDIR /app  
COPY package.json /app  
RUN npm install  
COPY . /app  
CMD yarn start  
EXPOSE 3000

