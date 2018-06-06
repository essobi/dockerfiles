FROM invoiceninja/invoiceninja  
MAINTAINER Louis-Rémi Babé <lrbabe@chez-nestor.com>  
  
# install payline plugin  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libxml2-dev \  
&& docker-php-ext-install soap \  
&& composer require chez-nestor/omnipay-payline:dev-master --working-dir
/var/www/app \--no-update \  
&& composer install --working-dir /var/www/app -o --no-dev --no-interaction
--no-progress  
  
VOLUME /var/www/app/public  
  
WORKDIR /var/www/app  
  
# Fix 'Failed to open stream: Permission denied' error \- Laravel  
# see http://stackoverflow.com/questions/23540083/failed-to-open-stream-
permission-denied-error-laravel  
# The --no-dev flag on the last line is here because the payline package
declares  
# test classes that do not exist :-(  
RUN php artisan cache:clear  

