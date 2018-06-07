FROM node:8 as builder  
  
WORKDIR /usr/src/app  
  
COPY package.json ./  
RUN yarn install  
  
COPY . ./  
RUN yarn run build  
  
FROM nginx  
  
WORKDIR /usr/share/nginx/html  
COPY \--from=builder /usr/src/app/public .  
COPY \--from=builder /usr/src/app/static .  
RUN chmod -R 0755 .

