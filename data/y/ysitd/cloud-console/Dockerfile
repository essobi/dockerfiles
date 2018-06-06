FROM node:8-alpine  
  
ADD . /app  
  
WORKDIR /app  
  
RUN yarn install && \  
yarn build && \  
yarn install --production  
  
CMD ["yarn", "start"]

