FROM node:8.9-alpine  
  
RUN npm install -g sails grunt bower  
  
RUN mkdir /2c_bikeroutes_ms  
WORKDIR /2c_bikeroutes_ms  
  
ADD . /2c_bikeroutes_ms  
  
ENV GOOGLE_MAPS_API_KEY="AIzaSyDkWzik2KXT-gc1mMdqHh2sPQzJX15fhcc"  
RUN npm cache verify  
  
RUN npm install -g  
  
EXPOSE 6002  
#EXPOSE 6005  
#CMD npm start  

