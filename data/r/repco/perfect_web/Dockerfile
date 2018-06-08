###############  
# perfect_web #  
###############  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
# File Author / Maintainer  
MAINTAINER Colin Hom  
  
# Update the repository  
RUN apt-get update  
  
# Install necessary tools  
RUN apt-get install -y nano wget dialog net-tools nginx-extras npm git ca-
certificates  
  
RUN npm install bower -g  
  
# Remove the default Nginx configuration file  
RUN rm -v /etc/nginx/nginx.conf  
  
# Copy a configuration file from the current directory  
ADD nginx.conf /etc/nginx/  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose ports  
EXPOSE 80  
ADD ./www/bower.json /var/www/bower.json  
  
WORKDIR /var/www  
  
#hopefully someone takes care of this soon (ehem bower)  
RUN apt-get install -y nodejs-legacy  
  
RUN bower install --allow-root  
  
VOLUME ["/var/log/nginx"]  
  
ADD ./www /var/www  
  
ENTRYPOINT ["nginx"]  

