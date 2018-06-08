FROM php:7.1.10-apache  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i 's/<\/VirtualHost>/LogFormat \"%{X-Forwarded-For}i %h %l %u
%t\\\"%r\\\\\" %>s %O \\\\\"%{Referer}i\\\\\" \\\\\"%{User-Agent}i\\\\\"\"
combined\n<\/VirtualHost>/' /etc/apache2/sites-available/000-default.conf && \  
ln -sf /dev/stdout /var/log/access.log && \  
ln -sf /dev/stderr /var/log/error.log  
COPY app.sh /app.sh  
COPY php.ini /usr/local/etc/php/  
RUN chmod +x /app.sh  
COPY 000-default.conf /etc/apache2/sites-available/  
RUN mkdir -p /app && rm -R /var/www/html && ln -s /app /var/www/html  
COPY files/ /app  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/app.sh"]  

