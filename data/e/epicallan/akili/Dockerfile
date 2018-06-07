FROM node:latest  
  
RUN mkdir /src  
  
WORKDIR /src  
ADD . /src  
RUN npm install --production  
  
EXPOSE 5000  
CMD npm run start-server  

