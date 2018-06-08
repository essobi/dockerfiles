# Dockerfile for last stable version of Nginx.  
FROM ubuntu:latest  
MAINTAINER Pablo Gillari Ces <pgillari@lyracons.com>  
  
# Avoid terminal dialog messages on Ubuntu/Debian containers.  
# Don't show errors when calling console.  
RUN export DEBIAN_FRONTEND=noninteractive && \  
export DEBCONF_NONINTERACTIVE_SEEN=true && \  
sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile  
  
# Common packages.  
RUN apt-get install -y vim curl wget  
  
# Installation.  
RUN apt-get update && \  
apt-get install -y nginx  
  
# Configuration.  
RUN usermod -u 1000 www-data && \  
rm -rf /etc/nginx/sites-enabled && \  
ln -s /etc/nginx/sites-available /etc/nginx/sites-enabled  
  
ADD ./virtualhost /etc/nginx/sites-available/default  
  
# Entrypoint.  
ADD ./entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
ENTRYPOINT ["/bin/bash", "/root/entrypoint.sh"]  

