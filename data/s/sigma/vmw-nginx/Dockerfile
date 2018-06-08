FROM stackbrew/ubuntu:saucy  
MAINTAINER Yann Hodique <hodiquey@vmware.com>  
  
# Install Nginx  
RUN apt-get update  
RUN apt-get install -y --force-yes software-properties-common  
RUN add-apt-repository ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -y --force-yes nginx curl  
  
# Install confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.5.0/confd-0.5.0-linux-
amd64 -o /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
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

