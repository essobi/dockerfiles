FROM node:8.6 as node  
  
WORKDIR /app  
COPY package.json /app/  
RUN npm install  
COPY ./ /app/  
RUN npm run build -- --sourcemap true  
  
# Stage 1, based on Nginx, to have only the compiled app, ready for production
with Nginx  
FROM nginx:1.13  
COPY \--from=node /app/dist/ /usr/share/nginx/html  
COPY deploy/nginx.conf /etc/nginx/nginx.conf  

