FROM node:8-alpine as builder  
  
# Use mirrors in china  
RUN echo https://mirrors.aliyun.com/alpine/v3.6/main > /etc/apk/repositories;
\  
echo https://mirrors.aliyun.com/alpine/v3.6/community >> /etc/apk/repositories  
  
# Add core packages to allow building native extensions  
RUN apk add --no-cache make gcc g++ python  
  
RUN npm install -g yarn  
  
WORKDIR /app  
  
COPY package.json yarn.lock /app/  
RUN yarn install  
  
COPY . /app  
  
RUN NODE_ENV=production yarn build  
  
FROM nginx:alpine  
  
COPY ./nginx/default.conf /etc/nginx/conf.d/  
COPY ./nginx/auth_basic /etc/nginx/auth_basic  
  
COPY \--from=builder /app/dist/ /var/www/html/web  

