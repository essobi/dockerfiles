FROM node:4.2.2  
ADD ./package.json /usr/src/package.json  
WORKDIR /usr/src  
  
RUN npm i -g grunt-cli  
RUN npm install  
ADD . /usr/src/  
WORKDIR /usr/src  
RUN npm install  
CMD node index.js  
EXPOSE 10100  

