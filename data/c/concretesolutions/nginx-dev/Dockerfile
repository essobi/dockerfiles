# Pull base image.  
FROM concretesolutions/ubuntu-dev  
  
# Install basic packages  
RUN apt-get update &&\  
apt-get -y install nginx &&\  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Add script to generate self signed certificates  
# Script from https://gist.github.com/bradland/1690807  
COPY /usr/bin/gencert /usr/bin/gencert  
RUN chmod +x /usr/bin/gencert  
  
# Enable SSL and setup a testing SSL virtualhost  
RUN gencert localhost  
COPY /etc/nginx/sites-available/default-ssl /etc/nginx/sites-
available/default-ssl  
RUN ln -s /etc/nginx/sites-available/default-ssl /etc/nginx/sites-
enabled/default-ssl  
  
# Start Nginx with "daemon off"  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose http and https ports  
EXPOSE 80 443  
CMD ["nginx"]  

