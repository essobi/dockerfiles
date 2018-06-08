FROM node:8.9.4-alpine as builder  
  
WORKDIR /app  
COPY package.json yarn.lock ./  
RUN yarn --silent install  
  
COPY . .  
RUN yarn run build  
  
FROM nginx:1.13.9-alpine  
COPY \--from=builder /app/build /usr/share/nginx/html  

