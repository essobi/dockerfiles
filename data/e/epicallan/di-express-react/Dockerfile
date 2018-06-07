FROM node:latest  
  
RUN mkdir /src  
  
WORKDIR /src  
ADD . /src  
ENV NODE_ENV production  
RUN npm install --production  
  
EXPOSE 8000  
CMD npm start  

