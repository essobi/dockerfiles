FROM nginx:latest  
MAINTAINER Thomas ILLIET <contact@thomas-illiet.fr>  
  
# Copy static file to working directory  
COPY build /usr/share/nginx/html  
  
# Start server by default  
CMD ["nginx", "-g", "daemon off;"]  

