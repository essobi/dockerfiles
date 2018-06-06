FROM node:8.6-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENV PORT=3000  
ADD ./package.json ./package.json  
ADD ./yarn.lock ./yarn.lock  
RUN yarn install  
  
ADD . .  
ENTRYPOINT yarn start  
  
EXPOSE 3000

