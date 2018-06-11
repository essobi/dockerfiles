FROM bitnami/minideb:stretch  
  
RUN install_packages gnupg2 curl ca-certificates  
  
RUN curl https://nginx.ru/keys/nginx_signing.key | apt-key add -  
RUN echo 'deb http://nginx.org/packages/mainline/debian/ stretch nginx' >>
'/etc/apt/sources.list.d/nginx.org.list' && \  
echo 'deb-src http://nginx.org/packages/mainline/debian/ stretch nginx' >>
'/etc/apt/sources.list.d/nginx.org.list'  
  
RUN install_packages nginx nginx-module-perl  
  
RUN rm -f /etc/nginx/conf.d/default.conf  
RUN mkdir -p /etc/nginx/sites-enabled && mkdir -p /etc/nginx/sites-available  
RUN rm -f /etc/nginx/sites-enabled/*  
  
ADD nginx.conf /etc/nginx/  
  
# Detailed error pages  
RUN mkdir /usr/share/nginx/html/nginx_error  
  
ADD http_error_codes.sh /usr/local/bin  
ADD make_error_inc.sh /usr/local/bin  
ADD make_error_pages.sh /usr/local/bin  
ADD docker_start_nginx.sh /usr/local/bin  
  
RUN /usr/local/bin/make_error_inc.sh  
RUN /usr/local/bin/make_error_pages.sh  
  
RUN usermod -u 1000 www-data  
  
CMD ["docker_start_nginx.sh"]  
  
STOPSIGNAL SIGTERM  
  
EXPOSE 80  

