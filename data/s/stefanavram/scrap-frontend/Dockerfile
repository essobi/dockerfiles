FROM nginx:alpine  
  
COPY nginx.conf /etc/nginx/conf.d/default.conf  
COPY dist/ /usr/share/nginx/html  
  
VOLUME /usr/share/nginx/html  
VOLUME /etc/nginx  
EXPOSE 80  

