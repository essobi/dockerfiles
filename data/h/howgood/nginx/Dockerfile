# howgood/nginx  
FROM nginx:1  
COPY mime.types /etc/nginx/  
COPY nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

