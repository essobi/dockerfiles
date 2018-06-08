FROM nginx:alpine  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY index.html /usr/share/nginx/html  
COPY ./dist /usr/share/nginx/html/dist/  
COPY health /usr/share/nginx/html  
  

