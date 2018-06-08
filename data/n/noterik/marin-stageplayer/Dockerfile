FROM node:6.11.0-alpine as builder  
WORKDIR /opt/app  
COPY . /opt/app/  
RUN npm config set registry https://registry.npmjs.org/  
RUN npm install  
RUN npm run build:prod  
  
FROM nginx:alpine  
COPY \--from=builder /opt/app/dist/online /usr/share/nginx/html/  
EXPOSE 80  

