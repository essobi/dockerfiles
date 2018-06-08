# This image will be based on the official Nginx docker image  
# to serve static contents  
FROM nginx  
MAINTAINER Lee Boonstra <lee.boonstra@sencha.com>  
  
# We copy over our build to the Nginx server  
COPY build/production/Client /usr/share/nginx/html  
  
# Tell Docker we are going to use this port  
EXPOSE 80  

