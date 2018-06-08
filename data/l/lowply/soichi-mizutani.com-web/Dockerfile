FROM node:latest AS builder  
WORKDIR /home/  
COPY ./src ./src  
COPY ./package.json .  
COPY ./webpack.config.js .  
RUN mkdir -p ./public/assets/build  
RUN npm install  
ENV NODE_ENV production  
RUN npm run build  
  
FROM nginx:alpine  
COPY \--from=builder /home/public/assets/build
/usr/share/nginx/html/assets/build  
COPY ./public /usr/share/nginx/html  
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf  
  
MAINTAINER Sho Mizutani <lowply@gmail.com>  

