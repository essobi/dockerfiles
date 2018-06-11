FROM node:7.7.1  
MAINTAINER teamvinyl <vinyl.proj@gmail.com>  
  
RUN mkdir -p /app  
  
WORKDIR /app  
  
ADD . /app  
  
RUN npm install -g gulp  
RUN npm install  
RUN gulp build  
  
COPY . /app  
  
EXPOSE 5002  
CMD [ "gulp", "start:dev" ]  

