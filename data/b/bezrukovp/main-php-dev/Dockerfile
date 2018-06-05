FROM bezrukovp/main-php-master  
MAINTAINER Pavel Bezrukov "bezrukov.ps@gmail.com"  
  
# Install developer utilities  
RUN apt-get -y -q install php5-xdebug php5-xhprof graphviz  
  
# set php5 dev conf  
ADD etc/php5/mods-available /etc/apache2/mods-available  
  
# RUN ln -s /etc/php5/mods-available/xdebug.ini
/etc/php5/fpm/conf.d/20-xdebug.ini  
# RUN ln -s /etc/php5/mods-available/xdebug.ini
/etc/php5/cli/conf.d/20-xdebug.ini  
# RUN ln -s /etc/php5/mods-available/xdebug.ini
/etc/php5/apache2/conf.d/20-xdebug.ini  
  
# RUN ln -s /etc/php5/mods-available/xhprof.ini
/etc/php5/fpm/conf.d/20-xhprof.ini  
# RUN ln -s /etc/php5/mods-available/xhprof.ini
/etc/php5/cli/conf.d/20-xhprof.ini  
# RUN ln -s /etc/php5/mods-available/xhprof.ini
/etc/php5/apache2/conf.d/20-xhprof.ini  
  
ADD etc/nginx/bx /etc/nginx/bx  
ADD etc/nginx/sites-available /etc/nginx/sites-available  
  
# Install web UI XHProf  
RUN cd /var/www  
RUN wget http://pecl.php.net/get/xhprof-0.9.4.tgz  
RUN gzip -d xhprof-0.9.4.tgz  
RUN tar -xvf xhprof-0.9.4.tar  
RUN rm -f xhprof-0.9.4.tgz xhprof-0.9.4.tar  
  
  

