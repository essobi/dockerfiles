FROM node:6  
MAINTAINER Di Weng  
  
RUN npm install -g gulp  
  
WORKDIR /app  
ADD package.json ./  
RUN npm install  
ADD . ./  
  
EXPOSE 8000  
CMD ["gulp"]  
  

