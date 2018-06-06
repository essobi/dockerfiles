FROM node:8-alpine AS build  
  
WORKDIR /usr/corpus2  
  
ADD *.json ./  
ADD *.lock ./  
RUN yarn install  
  
ADD . .  
RUN yarn run lint  
RUN yarn run bundle  
  
FROM nginx:alpine  
  
WORKDIR /usr/share/nginx/html  
COPY \--from=build /usr/corpus2/dist /usr/share/nginx/html/  
  
EXPOSE 80  

