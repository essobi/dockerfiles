FROM suckowbiz/nginx  
  
LABEL maintainer="Tobias Suckow <tobias@suckow.biz>"  
  
RUN apt-get install --quiet --quiet --yes --no-install-recommends \  
imagemagick \  
php-fpm \  
php-gd \  
php-mbstring \  
# Fixes error: Uncaught Error: Call to undefined function utf8_decode()  
php-xml \  
supervisor  
  
RUN \  
# path expected for fpm socket  
mkdir --parent /var/run/php \  
# Secure php processor to disallow execution of closes script if requestet php
can not be found.  
&& sed --in-place "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/7.2/fpm/php.ini \  
&& sed --in-place "s/;daemonize = yes/daemonize = no/g" /etc/php/7.2/fpm/php-
fpm.conf  
  
COPY context /  
ENV ENTRYPOINT_AS_ROOT=yes  
ENTRYPOINT ["/entrypoint.sh", "/start.sh", "/start-php.sh"]  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]

