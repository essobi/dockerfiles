FROM node:6  
MAINTAINER Dmitri Voronianski <dmitri.voronianski@gmail.com>  
  
RUN mkdir -p /usr/rob-api  
COPY . /usr/rob-api  
WORKDIR /usr/rob-api  
RUN npm install  
  
ENV PORT 3000  
EXPOSE $PORT  
  
CMD ["npm", "start"]  

