FROM ubuntu  
  
# Install Nginx.  
RUN apt-get update  
RUN apt-get install -y nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
EXPOSE 80  
CMD nginx  

