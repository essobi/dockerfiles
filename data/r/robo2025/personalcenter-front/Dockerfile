FROM nginx:alpine  
  
COPY program/dist/ /usr/share/nginx/html  
  
WORKDIR /usr/share/nginx/html  
  
CMD ["nginx", "-g", "daemon off;"]

