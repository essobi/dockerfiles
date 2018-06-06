FROM node:7.7.1  
MAINTAINER teamvinyl <vinyl.proj@gmail.com>  
  
RUN mkdir -p /app  
  
WORKDIR /app  
  
ADD . /app  
  
RUN npm install  
  
COPY . /app  
  
EXPOSE 3000  
CMD [ "npm", "start" ]

