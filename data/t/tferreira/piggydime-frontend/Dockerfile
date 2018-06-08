FROM node:7.3  
COPY . /opt/static  
WORKDIR /opt/static  
  
ENV API_URL "http://api:5000"  
RUN npm install -g yarn  
RUN yarn install  
  
EXPOSE 3000  
CMD yarn start  

