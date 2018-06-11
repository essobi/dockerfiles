# Pull base image.  
FROM dockerfile/ubuntu  
  
# Install Nginx.  
RUN apt-get update  
RUN apt-get install nginx curl -y  
RUN cd /usr/local/bin  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.5.0/confd-0.5.0-linux-
amd64 -o confd  
RUN chmod +x confd  
  
# Remove default configuration  
RUN rm /etc/nginx/sites-enabled/default  
  
# Create configuration template  
RUN mkdir -p /etc/confd/{conf.d,templates}  
ADD ./nginx.toml /etc/confd/conf.d/nginx.toml  
ADD ./nginx.tmpl /etc/confd/templates/nginx.tmpl  
  
# Script to run Confd  
ADD ./confd-watch /usr/local/bin/confd-watch  
RUN chmod +x /usr/local/bin/confd-watch

