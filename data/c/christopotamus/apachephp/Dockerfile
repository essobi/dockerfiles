FROM ubuntu:trusty  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php-pear \  
php-apc  
RUN apt-get update && apt-get -yq install sendmail && rm -rf
/var/lib/apt/lists/*  
  
RUN /usr/sbin/php5enmod mcrypt  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
RUN echo "zend_extension =
/usr/lib/php5/apache2/conf.d/ioncube_loader_lin_5.5.so" >>
/etc/php5/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **False**  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
COPY ioncube-files/ioncube_loader_lin_5.5.so /usr/lib/php5/apache2/conf.d/  
  
RUN mkdir -p /app && rm -rf /var/www/html && ln -s /app /var/www/html  
ADD teampasswordmanager /app  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/run.sh"]  
  

