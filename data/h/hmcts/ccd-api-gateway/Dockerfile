FROM node:8.9.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json yarn.lock /usr/src/app/  
RUN yarn install  
  
COPY app.js server.js /usr/src/app/  
COPY app /usr/src/app/app  
COPY config /usr/src/app/config  
  
ENV PORT 3453  
HEALTHCHECK \--interval=10s --timeout=10s --retries=10 CMD http_proxy="" curl
--silent --fail http://localhost:3453/health  
  
EXPOSE 3453  
CMD [ "yarn", "start" ]  

