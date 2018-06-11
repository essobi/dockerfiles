##################################################  
#  
# Dockerfile for NginX  
#  
###################################################  
  
FROM unisis/base  
MAINTAINER Unisis <contacto@unisis.com.ar>  
  
# Expose ports 80 and 443 (80 is used to redirect to 443)  
EXPOSE 80 443  
  
VOLUME ["/etc/nginx/certs", "/var/log/nginx"]  
  
# Install NginX  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
openssh-server \  
nginx  
  
# Copy config files  
ENV CONF_REFRESHED_AT 2016_04_25  
ADD config/nginx.conf /root/nginx.conf  
ADD config/nginx-vhost.conf /root/nginx-vhost.conf  
  
# Copy NginX setup script  
ADD scripts/nginx-setup /usr/sbin/nginx-setup  
RUN chmod +x /usr/sbin/nginx-setup  
  
# Copy NginX service script  
ADD scripts/nginx-service /etc/init.d/nginx  
RUN chmod +x /etc/init.d/nginx  
  
# Copy start script  
ADD scripts/start.sh /root/start.sh  
RUN chmod +x /root/start.sh  
  
# Start script  
CMD ["/root/start.sh"]  

