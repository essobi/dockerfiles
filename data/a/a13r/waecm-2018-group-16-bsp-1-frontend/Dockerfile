# Stage 0, based on Node.js, to build and compile Angular  
FROM node:8.4 as node  
WORKDIR /app  
ADD package.json package-lock.json /app/  
RUN npm install  
ADD ./ /app/  
RUN npm run build  
  
# Stage 1, based on Nginx, to have only the compiled app, ready for production
with Nginx  
FROM nginx:1.13  
COPY \--from=node /app/dist/ /usr/share/nginx/html  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 8081  

