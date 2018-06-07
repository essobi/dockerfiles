FROM node:latest as builder  
WORKDIR /usr/src/app  
COPY package*.json ./  
RUN yarn  
COPY . .  
RUN yarn build  
  
FROM node:slim  
WORKDIR /usr/app  
COPY \--from=builder /usr/src/app/build .  
RUN yarn global add serve  
EXPOSE 5000  
CMD [ "serve" ]  

