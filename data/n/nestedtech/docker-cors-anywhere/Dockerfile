FROM node:8-alpine  
MAINTAINER Darren Oakley <darren@nested.com>  
  
ENV PORT 9000  
ENV APP_DIR /app  
  
RUN mkdir $APP_DIR  
WORKDIR $APP_DIR  
  
COPY package.json package.json  
COPY package-lock.json package-lock.json  
  
RUN npm install  
  
COPY index.js index.js  
  
EXPOSE 9000  
CMD ["npm", "start"]  

