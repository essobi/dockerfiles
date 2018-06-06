# docker build -t kalabox/mariadb .  
FROM kricker/mysql-base:latest  
  
RUN \  
apk add -U apache2 php-apache2 php-mysqli php-zip php-zlib php-bz2 php-ctype
php-gd php-mcrypt php-json && \  
rm -fr /var/cache/apk/*  
  
RUN mkdir -p /srv/www  
  
# RUN useradd -rm ruby_dev -u 1000 -g 50  
# don't add source code, going to mount it  
# ADD . /srv/www/siteroot  
RUN mkdir /data && chown -R apache:apache /data  
RUN mv /var/www/localhost/htdocs/index.html /data/index.html  
RUN rm -r /var/www/localhost/htdocs  
RUN ln -s /data /srv/www/siteroot && ln -s /data /var/www/localhost/htdocs  
RUN echo "The code for your application lives here. This will link directly to
your site root folder." > /data/README.txt  
VOLUME ["/data"]  
  
# www  
ADD www.conf /etc/apache2/sites-available/www.conf  
  
# sites-common  
ADD wwww /etc/apache2/sites-common/wwww  
  
# Alternative to a2ensite command  
RUN mkdir -p /etc/httpd/conf.d  
RUN ln -s /etc/httpd/sites-available/www /etc/httpd/conf.d/www  
RUN ln -s /etc/httpd/sites-available/000-default /etc/httpd/conf.d/000-default  
RUN ln -s /etc/httpd/sites-available/usertrack /etc/httpd/conf.d/usertrack  
RUN ln -s /etc/httpd/sites-available/proxy_http /etc/httpd/conf.d/proxy_http  
  
# Make apache start and be monitored by runit  
RUN mkdir -p /etc/service/apache  
ADD apache.sh /etc/service/apache/run  
RUN chmod +x /etc/service/apache/run  
  
COPY mini-server-base-start.sh /root/mini-server-base-start.sh  
RUN chmod 777 /root/mini-server-base-start.sh  
  
EXPOSE 80 22 443 11211  
# Define default command.  
ENTRYPOINT sh /root/mini-server-base-start.sh  

