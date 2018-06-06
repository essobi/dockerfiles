# Set nginx base image  
FROM nginx  
  
# Copy custom configuration file from the current directory  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx-verbling.conf /etc/nginx/nginx-default.conf  
  
# Copy static files to the static directory  
COPY static /static  

