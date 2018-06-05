FROM node:8-alpine  
  
WORKDIR /app  
  
ADD . /app  
  
RUN yarn install && \  
yarn build && \  
yarn install --production  
  
ENV NODE_ENV production  
  
CMD ["yarn", "start"]  

