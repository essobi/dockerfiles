FROM php:5.6-apache  
MAINTAINER Daniel Palstra <daniel@danielpalstra.com>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends unzip libmcrypt-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install \mcrypt pdo mysql mbstring && \  
a2enmod rewrite  
  
RUN rm -rf /var/www/html/*  
RUN curl -L https://github.com/InvoicePlane/InvoicePlane/archive/v1.4.5.tar.gz
| tar xz --strip-components=1  
RUN mv htaccess .htaccess  
RUN curl -O
http://translations.invoiceplane.com/download/project/fusioninvoice.zip &&
unzip fusioninvoice.zip -d tmp-lang/ && mv tmp-lang/*/* application/language/
&& rm -rf tmp-lang fusioninvoice.zip  
  
COPY invoice-plane-docker-config-files/database.php
application/config/database.php  
COPY invoice-plane-docker-config-files/init-invoicePlane.sh /usr/local/bin/  
  
RUN usermod -u 1000 www-data && \  
chmod o+w -R uploads application/config application/config/config.php
application/helpers/mpdf/tmp \  
application/helpers/mpdf/ttfontdata application/helpers/mpdf/graph_cache
application/logs  
  
VOLUME /var/www/html/uploads  
  
ENTRYPOINT ["init-invoicePlane.sh"]  
CMD ["apache2-foreground"]  

