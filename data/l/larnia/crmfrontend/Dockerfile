FROM node:6.9.0  
MAINTAINER Larnia.com  
  
# Create app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY package.json /app/  
COPY prodServer.js /app/  
COPY .babelrc /app/  
COPY webpack.config.prod.js /app/  
COPY tools /app/tools/  
COPY src /app/src/  
  
EXPOSE 80  
RUN npm install  
CMD npm run build && node prodServer.js

