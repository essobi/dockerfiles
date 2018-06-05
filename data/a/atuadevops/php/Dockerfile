FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y software-properties-common git vim  
  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y  
RUN apt-get update  
RUN apt-get install --allow-unauthenticated -y apache2 libapache2-mod-php5.6  
RUN apt-get install --allow-unauthenticated -y php5.6 php5.6-gd php5.6-cgi
php5.6-curl php5.6-json php5.6-pgsql \  
php5.6-xdebug php5.6-soap php5.6-xml php5.6-imap php5.6-imagick \  
php5.6-mbstring php5.6-zip php5.6-mcrypt  
  
RUN phpenmod mcrypt  
RUN apt-get install -y build-essential unzip xmlsec1 zip libxmlsec1
libxmlsec1-openssl  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y postfix >> /dev/null ||
:  
ADD config/postfix/filtro /etc/postfix/  
ADD config/postfix/main.cf /etc/postfix/  
  
RUN rm -rf /etc/php/5.6/apache2/php.ini  
ADD config/php/php.ini /etc/php/5.6/apache2/  
  
RUN rm -rf /etc/php/5.6/cgi/php.ini  
ADD config/php/php.ini /etc/php/5.6/cgi/  
  
RUN rm -rf /etc/php/5.6/cli/php.ini  
ADD config/php/cli/php.ini /etc/php/5.6/cli/  
  
RUN rm -rf /etc/php/5.6/apache2/conf.d/20-xdebug.ini  
ADD config/php/20-xdebug.ini /etc/php/5.6/apache2/conf.d/  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php; \  
mv composer.phar /usr/local/bin/composer; \  
chmod +x /usr/local/bin/composer  
  
ADD config/start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
CMD ["/usr/local/bin/start.sh"]  

