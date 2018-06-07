FROM mhart/alpine-node:7.1.0  
EXPOSE 8081  
RUN mkdir /app  
WORKDIR /app  
ENV NODE_ENV development  
  
COPY package.json /app  
RUN npm install  
  
COPY . /app  
RUN node_modules/.bin/gulp build-for-production  
  
CMD ["npm", "start"]  

