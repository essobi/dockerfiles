FROM node:7.9.0  
MAINTAINER Superbalist <tech+docker@superbalist.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN yarn install  
  
COPY src /usr/src/app/src/  
  
EXPOSE 3000  
CMD ["node", "./src/bin/www"]  

