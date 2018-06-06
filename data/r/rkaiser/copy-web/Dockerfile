FROM ubuntu:14.04  
# new ubuntu causes error: FROM ubuntu:17.10  
# Install Nginx  
# Add the repo to your apt sources  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ `lsb_release -cs`
nginx\ndeb-src http://nginx.org/packages/mainline/ubuntu/ `lsb_release -cs`
nginx" > /etc/apt/sources.list.d/nginx.list  
  
# Add application repository URL to the default sources  
# Older version  
# RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe" >>
/etc/apt/sources.list  
# Update the repository  
RUN apt-get update  
  
# Install necessary tools  
RUN apt-get install -y nano wget dialog net-tools  
  
# Download and Install Nginx  
RUN apt-get install -y nginx --force-yes  
  
# Remove the default Nginx configuration file  
RUN rm -v /etc/nginx/nginx.conf  
  
# Copy a configuration file from the current directory  
ADD compose/nginx.conf /etc/nginx/  
  
# Copy static files to public folder  
COPY dist /public/  
  
# Append "daemon off;" to the beginning of the configuration  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose ports  
EXPOSE 80 443  
# Set the default command to execute  
# when creating a new container  
CMD service nginx start  

