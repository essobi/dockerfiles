FROM debian:sid  
RUN apt-get update && \  
apt-get install -y nginx && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
RUN rm -rf /etc/nginx/*.d /etc/nginx/sites-* && \  
mkdir -p /etc/nginx/addon.d /etc/nginx/config.d /etc/nginx/host.d
/etc/nginx/nginx.d  
ADD etc /etc  
ADD supervisord.conf /etc/supervisor/conf.d/nginx.conf  
EXPOSE 80  

