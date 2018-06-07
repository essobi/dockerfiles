FROM scratch  
MAINTAINER Jake Sanders <jake@livewyer.com>  
  
ADD rootfs.tar.gz /  
  
ADD php-fpm.conf /etc/php-fpm.conf  
RUN addgroup nobody && mkdir /srv && mkdir /srv/website && echo "<h1>It
works!</h1>" > /srv/website/index.html && echo "<?php phpinfo();" >
/srv/website/index.php && chmod -R 0666 /srv/website  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin
--filename=composer  
  
EXPOSE 9000  
CMD ["php-fpm", "-F", "-R"]  

