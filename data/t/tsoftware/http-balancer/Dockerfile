FROM ubuntu:14.04  
MAINTAINER Tsoftware  
  
# Install Nginx  
RUN apt-get install -y --force-yes software-properties-common  
RUN add-apt-repository ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -y --force-yes nginx curl  
  
# Install confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-
amd64 > confd  
RUN mv confd /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
# Create directories  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
  
# Remove default site  
RUN rm -f /etc/nginx/sites-enabled/default  
  
# Add template for Confd Nginx TOML file  
ADD ./nginx-conf-tmpl.template /opt/nginx-conf-tmpl.template  
  
# Add template for Nginx configuration template  
ADD ./nginx-toml.template /opt/nginx-toml.template  
  
# Add boot script  
ADD ./boot.sh /opt/boot.sh  
RUN chmod +x /opt/boot.sh  
  
# Add boot script  
ADD ./prepare-and-start.sh /opt/prepare-and-start.sh  
RUN chmod +x /opt/prepare-and-start.sh  
  
# Create templates and run the boot script  
ENTRYPOINT ./opt/prepare-and-start.sh  

