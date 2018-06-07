FROM node:latest  
  
RUN mkdir /src  
  
WORKDIR /src  
ADD . /src  
RUN npm install --production  
  
EXPOSE 3000  
CMD NODE_ENV=production npm start  

