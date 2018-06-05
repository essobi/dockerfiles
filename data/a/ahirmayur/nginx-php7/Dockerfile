FROM ahirmayur/ubuntu  
MAINTAINER Mayur Ahir "https://github.com/ahirmayur"  
# Default lang is REAL English ;)  
ENV LANG C.UTF-8  
RUN echo "LC_ALL=en_GB.UTF-8" >> /etc/default/locale  
RUN locale-gen en_GB.UTF-8  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN add-apt-repository -y ppa:nginx/stable  
RUN add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update  
  
RUN apt-get install -y supervisor nginx php7.0 php7.0-fpm php7.0-mysql
php7.0-curl php7.0-json dos2unix pwgen  
  
# Tweak nginx config  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Shell script must run the daemon without letting it daemonize/fork it  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf  
  
# Set listen port  
RUN sed -i 's/listen = \/run\/php\/php7.0-fpm.sock/;listen =
\/run\/php\/php7.0-fpm.sock\nlisten = 127.0.0.1:9000/g'
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i "s/;listen.allowed_clients = 127.0.0.1/listen.allowed_clients =
127.0.0.1/" /etc/php/7.0/fpm/pool.d/www.conf  
  
# Security  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.0/fpm/php.ini  
  
RUN rm -rf /etc/nginx/sites-enabled/default  
ADD sources/site /etc/nginx/sites-available/  
  
RUN ln -s /etc/nginx/sites-available/site /etc/nginx/sites-enabled/site  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
ADD sources/info.php /var/www/  
  
ADD sources/start.sh /start.sh  
RUN dos2unix -k -o /start.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/start.sh"]  
  
CMD nginx && php-fpm  

