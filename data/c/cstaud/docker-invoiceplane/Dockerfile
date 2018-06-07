FROM php:7-apache  
MAINTAINER Christian Staude <info@cstaud.de>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends unzip libmcrypt-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install \mcrypt mysqli mbstring && \  
a2enmod rewrite  
  
RUN rm -rf /var/www/html/*  
RUN rm -rf /usr/src/*  
VOLUME ["/var/www/html"]  
  
RUN usermod -u 1000 www-data  
WORKDIR /usr/src  
  
RUN curl -L https://github.com/InvoicePlane/InvoicePlane/archive/v1.4.8.tar.gz
| tar xz --strip-components=1  
RUN mv htaccess .htaccess  
  
RUN curl -O
http://translations.invoiceplane.com/download/project/fusioninvoice.zip && \  
unzip fusioninvoice.zip -d tmp-lang/ && mv tmp-lang/*/* application/language/
&& \  
rm -rf tmp-lang fusioninvoice.zip  
  
WORKDIR /var/www/html  
COPY invoice-plane-docker-config-files/init-invoicePlane.sh /usr/local/bin/  
ENTRYPOINT ["init-invoicePlane.sh"]  
CMD ["apache2-foreground"]  

