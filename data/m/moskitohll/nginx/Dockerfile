FROM nginx  
  
# Copy a configuration file from the current directory  
ADD nginx.conf /etc/nginx/  
  
# Append "daemon off;" to the beginning of the configuration  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN mkdir /etc/nginx/sites-enabled  
RUN mkdir /etc/nginx/ssl  
# Expose ports  
#EXPOSE 80  
EXPOSE 443  
VOLUME ["etc/nginx/sites-enabled/","/etc/nginx/ssl"]  
  
# Set the default command to execute  
# when creating a new container  
CMD service nginx start  

