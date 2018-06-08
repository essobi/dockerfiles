FROM ubuntu:12.04  
MAINTAINER Raphael Gyory <xellessprl@gmail.com>  
  
  
# Install Nginx  
RUN apt-get -y update  
RUN apt-get install -y --force-yes nginx curl  
  
# Install confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.3.0/confd_0.3.0_linux_amd64.tar.gz
| tar xz  
RUN mv confd /usr/local/bin/confd  
  
# Create directories  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
  
# Add confd files  
ADD ./nginx.conf.tmpl /etc/confd/templates/nginx.conf.tmpl  
ADD ./nginx.toml /etc/confd/conf.d/nginx.toml  
  
# Remove default site  
RUN rm -f /etc/nginx/sites-enabled/default  
  
# Add boot script  
ADD ./boot.sh /opt/boot.sh  
RUN chmod +x /opt/boot.sh  
  
# Run the boot script  
CMD /opt/boot.sh  

