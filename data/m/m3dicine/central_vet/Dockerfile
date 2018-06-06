#docker file  
FROM node:6-alpine  
  
RUN mkdir -p /usr/core  
RUN mkdir -p /usr/core/stage  
RUN mkdir -p /usr/core/ssl  
  
COPY index.js /usr/core  
COPY stage /usr/core/stage  
COPY package.json /usr/core  
COPY sslcert /usr/core/sslcert  
  
WORKDIR /usr/core  
RUN npm install --production  
RUN ls stage  
EXPOSE 443  
CMD ["node","index.js"]  

