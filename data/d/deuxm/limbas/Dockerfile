FROM centos:7  
MAINTAINER Arne Bosien  
  
RUN yum -y install httpd php php-gd php-imap php-odbc php-soap php-xml php-
ctype php-mbstring unixODBC \  
postgresql-odbc postgresql ImageMagick poppler-utils pdftohtml \  
perl-Image-ExifTool wget unzip t1lib  
  
# install limbas  
RUN wget -qO-
https://sourceforge.net/projects/limbas/files/limbas%20source%20package/3.x/openlimbas_3.3.16.345.tar.gz/download
| tar xvz -C /var/www/html/  
RUN chown -R apache:apache /var/www/html/  
  
# change configs in php.ini  
RUN sed -i 's/short_open_tag =.*/short_open_tag = On/g' /etc/php.ini && \  
sed -i 's/error_reporting =.*/error_reporting =
E_COMPILE_ERROR|E_ERROR|E_CORE_ERROR/g' /etc/php.ini && \  
sed -i 's/upload_max_filesize =.*/upload_max_filesize = 10M/g' /etc/php.ini &&
\  
sed -i 's/post_max_size =.*/post_max_size = 16M/g' /etc/php.ini && \  
sed -i 's/;date.timezone.*/date.timezone = Europe\/Berlin/g' /etc/php.ini  
  
# add parameters to php.ini  
RUN echo 'register_globals = Off' >> /etc/php.ini && \  
echo 'magic_quotes_gpc = off' >> /etc/php.ini && \  
echo 'max_input_vars = 10000' >> /etc/php.ini  
  
# remove line  
RUN sed -i 's/AddDefaultCharset UTF-8//g' /etc/httpd/conf/httpd.conf  
  
# add to http config  
RUN echo $'\n\  
<Directory "/var/www/html/openlimbas/dependent">\n\  
AllowOverride All \n\  
</Directory>' >> /etc/httpd/conf/httpd.conf  
  
# rename driver to limbas default  
RUN sed -i 's/PostgreSQL/PSQL/g' /etc/odbcinst.ini  
  
# run httpd  
EXPOSE 80  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  

