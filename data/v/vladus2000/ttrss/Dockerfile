FROM vladus2000/arch-base  
MAINTAINER vladus2000 <docker@matt.land>  
  
COPY shiz/ /  
  
RUN pacman -Syyu \--noconfirm \--needed && \  
groupadd -g 89 mysql && \  
useradd -u 89 -g mysql mysql && \  
pacman -S \--noconfirm \--needed tt-rss nginx mariadb php-fpm && \  
rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/sync/* && \  
mv nginx.conf /etc/nginx/. && \  
ln -s /usr/share/webapps/tt-rss /usr/share/nginx/html/tt-rss && \  
mv config.php /usr/share/nginx/html/tt-rss/. && \  
chown -R http:http /usr/share/nginx/html/tt-rss/ && \  
sed -e
's/;extension=iconv/extension=iconv/;s/;extension=mysqli/extension=mysqli/;s/;extension=pdo_mysql/extension=pdo_mysql/'
/etc/php/php.ini > /t && \  
mv /t /etc/php/php.ini && \  
chmod +x /startup.sh  
  
CMD /bin/bash -c /startup.sh  

