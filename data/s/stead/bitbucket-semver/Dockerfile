FROM node:8.5.0-alpine  
  
LABEL maintainer=https://github.com/mikestead  
  
WORKDIR /opt/app  
  
COPY package.json yarn.lock ./  
RUN yarn install --production  
COPY . ./  
  
ENTRYPOINT ["node", "run.js"]  

