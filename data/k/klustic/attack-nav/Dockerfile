FROM node:9-alpine AS builder  
RUN apk add --no-cache git  
RUN git clone https://github.com/mitre/attack-navigator /opt/attack-navigator  
WORKDIR /opt/attack-navigator/nav-app  
RUN npm install  
RUN npm i -g @angular/cli  
RUN ng build  
  
FROM nginx:alpine  
EXPOSE 80  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY \--from=builder /opt/attack-navigator/nav-app/dist/ /webroot/  

