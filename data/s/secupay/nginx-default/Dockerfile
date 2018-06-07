FROM nginx:1  
RUN rm /etc/nginx/conf.d/default.conf  
COPY www.conf /etc/nginx/conf.d/  
  
# switch user from nginx to www-user  
RUN sed -i 's/^user.*/user www-data;/' /etc/nginx/nginx.conf

