FROM node:9.3-alpine  
RUN mkdir -p /mustachebash  
WORKDIR /mustachebash  
COPY package.json package-lock.json ./  
RUN apk add --no-cache python make g++ && \  
npm install --production --no-optional && \  
npm cache clean --force && \  
apk del --purge python make g++  
  
COPY lib lib  
EXPOSE 4000  
CMD npm start  

