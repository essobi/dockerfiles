FROM php:5.6-apache  
  
RUN rm -rf /var/www/html/*  
RUN curl -L https://github.com/InvoicePlane/InvoicePlane/archive/v1.4.3.tar.gz
| tar xz --strip-components=1  
  
RUN a2enmod rewrite  
RUN docker-php-ext-install pdo mysql mbstring  
  
RUN apt-get update  
RUN apt-get install libmcrypt-dev -y  
RUN docker-php-ext-install mcrypt  
  
RUN apt-get install nano -y  
ENV TERM=xterm  
  
RUN apt-get install wget unzip -y  
RUN wget
http://translations.invoiceplane.com/download/project/fusioninvoice.zip &&
unzip fusioninvoice.zip -d tmp-lang/ && mv tmp-lang/*/* application/language/
&& rm -rf tmp-lang fusioninvoice.zip  
  
COPY invoice-plane-docker-config-files/database.php
application/config/database.php  
COPY invoice-plane-docker-config-files/init-invoicePlane.sh /usr/local/bin/  
RUN mv index.php trueIndex.php  
COPY invoice-plane-docker-config-files/domainCatcher.php index.php  
RUN chmod o+w . index.php trueIndex.php application/config/config.php  
  
RUN usermod -u 1000 www-data  
RUN chmod o+w -R uploads application/config/database.php
application/helpers/mpdf/tmp application/logs  
  
VOLUME /var/www/html/uploads  
CMD ["init-invoicePlane.sh"]  

