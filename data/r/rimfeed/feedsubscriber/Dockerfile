FROM node:0.10  
COPY . /src  
  
WORKDIR /src  
  
RUN npm install  
  
RUN ./node_modules/.bin/grunt  
  
CMD node server.js | ./node_modules/.bin/bunyan -o short  

