FROM jtabet/php-ext-sockets  
MAINTAINER Jérémie Tabet <dev@jeremie.tabet.rocks>  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php --
--install-dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer  

