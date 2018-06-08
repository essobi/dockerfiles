FROM node:6.3  
MAINTAINER ukatama dev.ukatama@gmail.com  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY nekodev /usr/src/app/nekodev  
COPY package.json /usr/src/app  
  
RUN npm install  
  
COPY . /usr/src/app  
RUN npm run production  
  
EXPOSE 80  
CMD ["npm", "start"]  

