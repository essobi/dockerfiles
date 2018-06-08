FROM nginx:1.9.10  
MAINTAINER skyscrapers "support@skyscrapers.eu"  
WORKDIR /tmp  
  
# Apply Nginx configuration  
ADD ./config/nginx.conf /opt/etc/nginx.conf  
ADD ./config/fastcgi.conf /etc/nginx/fastcgi.conf  
ADD ./config/laravel /etc/nginx/sites-enabled/laravel  
# Nginx startup script  
ADD config/nginx-start.sh /opt/bin/nginx-start.sh  
  
RUN chmod u=rwx /opt/bin/nginx-start.sh && \  
mkdir -p /data && \  
rm /etc/nginx/conf.d/default.conf && \  
apt-get clean  
  
VOLUME ["/data"]  
  
WORKDIR /data  
CMD ["/opt/bin/nginx-start.sh"]

