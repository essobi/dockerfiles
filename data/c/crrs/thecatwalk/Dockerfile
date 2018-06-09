FROM nginx  
RUN apt-get update -y ; apt-get install -y php5-curl php5-gd php5-mysql
php5-fpm git supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY /default.conf /etc/nginx/conf.d/  
COPY /nginx.conf /etc/nginx/nginx.conf  
COPY / /usr/share/nginx/html  
RUN chown -R www-data /usr/share/nginx/html ; rm
/usr/share/nginx/html/index.html  
EXPOSE 80 443  
CMD /usr/bin/supervisord  

