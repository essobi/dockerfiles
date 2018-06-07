FROM nginx:stable-alpine  
ADD src /html  
COPY nginx.conf /etc/nginx/nginx.conf  
CMD ["nginx", "-g", "daemon off;"]  

