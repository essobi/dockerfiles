FROM 2dotstwice/nginx  
  
MAINTAINER Kristof Coomans "kristof@2dotstwice.be"  
ENV REFRESHED_AT "2017-02-04 11:13:00"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install software-properties-
common  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing -q install
php5.6-fpm php5.6-gd php5.6-sqlite php5.6-mysqlnd php5.6-curl php5.6-intl
php5.6-xml php5.6-mbstring php5.6-opcache php5.6-json php5.6-mcrypt
php5.6-bcmath php5.6-soap php5.6-zip  
  
ENV CONFIG_REFRESHED_AT "2017-02-04 11:13:00"  
# php configuration  
ADD ./files/etc/php5/fpm/conf.d/99-custom.ini
/etc/php/5.6/fpm/conf.d/99-custom.ini  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/5.6/fpm/php.ini  
  
# php-fpm configuration  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/5.6/fpm/php-
fpm.conf  
RUN mkdir /run/php  
  
# supervisor configuration for php-fpm  
ADD ./files/etc/supervisor/conf.d/php-fpm.conf /etc/supervisor/conf.d/php-
fpm.conf  
  
# nginx site configuration for php-fpm  
ADD ./files/etc/nginx/sites-available/default /etc/nginx/sites-
available/default  
  
# Standard hosting package nginx configuration  
# Reduce worker processes to 2, it's just a small site with not much traffic.  
RUN sed -i -e "s/worker_processes 4/worker_processes 2/g"
/etc/nginx/nginx.conf  
  
# Standard hosting package php-fpm configuration  
ADD ./files/etc/php5/fpm/pool.d/www.conf /etc/php/5.6/fpm/pool.d/www.conf  

