FROM tatoonz/nginx-php-fpm  
  
MAINTAINER TaToonz (peerapath.t@gmail.com)  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
software-properties-common  
  
# install phalcon  
RUN apt-add-repository ppa:phalcon/stable \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
php5-phalcon \  
&& php5enmod phalcon  
  
RUN apt-get purge -y --auto-remove \  
software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install phalcon devtools  
RUN composer global require phalcon/devtools:dev-master \  
&& ln -s ~/.composer/vendor/phalcon/devtools/phalcon.php /usr/bin/phalcon \  
&& chmod ugo+x /usr/bin/phalcon

