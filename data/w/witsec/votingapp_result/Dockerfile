FROM node:8.9-alpine  
MAINTAINER witsec <mark@witsec.nl>  
  
RUN mkdir -p /app  
WORKDIR /app  
  
RUN npm install -g nodemon  
RUN npm config set registry https://registry.npmjs.org  
  
COPY app/package.json /app/package.json  
  
RUN npm install \  
&& npm ls \  
&& npm cache clean --force \  
&& mv /app/node_modules /node_modules  
  
COPY app/ /app/  
  
ENV PORT 80  
EXPOSE 80  
CMD ["node", "server.js"]  

