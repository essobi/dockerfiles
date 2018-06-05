FROM node:7-alpine  
  
WORKDIR /usr/src/app  
ENV API_URL https://b0ckfkhfig.execute-api.eu-west-1.amazonaws.com/prod/submit  
  
ADD package.json .  
RUN npm install --only=production  
  
ADD . /usr/src/app  
  
ENTRYPOINT [ "node", "index.js" ]  

