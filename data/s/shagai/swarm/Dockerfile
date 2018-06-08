FROM node:8.8.1-slim  
  
RUN mkdir /src  
  
ADD ./src /src  
WORKDIR /src  
RUN npm install  
  
EXPOSE 3000  
CMD npm run start  

