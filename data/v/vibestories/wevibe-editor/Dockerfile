FROM node:latest AS build  
LABEL Author="Charles Stover"  
ENV NODE_ENV production  
WORKDIR /var/www/  
COPY package*.json /var/www/  
RUN npm install  
COPY . /var/www/  
RUN npm run build  
FROM nginx:latest  
EXPOSE 80  
COPY \--from=build /var/www/build /usr/share/nginx/html/  

