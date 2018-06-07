############################################################  
# Dockerfile to build Nginx Installed Containers  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Lax  
  
# Install Nginx  
  
# Update the repository  
RUN apt-get update  
  
# Download and Install Nginx  
RUN apt-get install -y nginx  
  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]  

