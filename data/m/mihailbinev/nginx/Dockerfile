FROM debian  
MAINTAINER Mihail Binev <mihail@kodeart.com>  
  
# install supervisor and nginx  
RUN apt-get update && apt-get -y install supervisor nginx --no-install-
recommends  
  
# cleanup  
RUN apt-get -y autoremove && apt-get autoclean && apt-get clean && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# set permissions for www-data  
RUN usermod -u 1000 www-data && usermod -a -G 50 www-data && \  
chmod 700 /var/www && \  
chown -R www-data:www-data /var/www/  
  
# add conf files for supervisor and nginx  
ADD config-files /  
RUN ln -s /etc/nginx/sites-available/varwww.conf /etc/nginx/sites-
enabled/varwww && \  
rm /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default  
  
# define mountable directories  
VOLUME ["/var/www", "/etc/nginx/conf.d", "/etc/nginx/sites-enabled",
"/etc/nginx/certs", "/var/log/nginx"]  
  
EXPOSE 80 443  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

