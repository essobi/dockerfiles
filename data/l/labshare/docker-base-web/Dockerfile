FROM nginx  
  
# Create app directory  
WORKDIR /var/www/app  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
# Install app dependencies  
COPY app-nginx.conf /etc/nginx/conf.d  
  
EXPOSE 8000  

