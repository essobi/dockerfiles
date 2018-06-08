FROM ubuntu:14.04  
MAINTAINER Morgan Blackthorne <morgan@windsofstorm.net>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/stormerider/rancher-wpmu-nginx-
trusty.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.4.9"  
  
RUN date  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install NewRelic support  
ADD https://download.newrelic.com/548C16BF.gpg /newrelic.gpg  
RUN apt-key add /newrelic.gpg  
RUN echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list  
  
# Update and upgrade  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Basic Requirements  
RUN apt-get -y install mysql-client nginx php5-fpm php5-mysql php-apc pwgen
python-setuptools curl unzip php5-curl php5-gd php5-intl php-pear php5-imagick
php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode
php5-sqlite php5-tidy php5-xmlrpc php5-xsl bzip2 xz-utils zip newrelic-php5  
  
# nginx config  
ADD ./config/nginx-core.conf /etc/nginx/nginx.conf  
ADD ./config/fastcgi_params.conf /etc/nginx/fastcgi_params  
  
# php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
# Ideally this should be 0660, but until I can track down why www-data can't
talk to /var/run/php-fpm.sock, make it 0666  
RUN sed -i -e "s/;listen.mode\s*=\s0660/listen.mode = 0666/g"
/etc/php5/fpm/pool.d/www.conf  
RUN find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
ADD ./config/www.conf /etc/php5/fpm/pool.d/www.conf  
  
# nginx site conf  
RUN rm /etc/nginx/sites-enabled/default  
ADD ./config/nginx-site.conf /etc/nginx/sites-enabled/default  
  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./config/supervisord.conf /etc/supervisord.conf  
  
# Enable shell access for www-data user  
RUN /usr/bin/chsh -s /bin/bash www-data  
  
# Install Wordpress  
ADD https://wordpress.org/latest.tar.gz /usr/share/nginx/latest.tar.gz  
RUN cd /usr/share/nginx/ && tar xf latest.tar.gz && rm latest.tar.gz  
RUN mv /usr/share/nginx/html/5* /usr/share/nginx/wordpress  
RUN rm -rf /usr/share/nginx/www  
RUN mv /usr/share/nginx/wordpress /usr/share/nginx/www  
RUN chown -R www-data:www-data /usr/share/nginx/www  
  
# Install WP CLI  
RUN curl https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar -o /usr/local/bin/wp  
RUN chmod +x /usr/local/bin/wp  
RUN ln -s /usr/share/nginx/www /var/www  
  
# Wordpress Initialization and Startup Script  
ADD ./scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
ADD ./scripts/wpdl.sh /wpdl.sh  
RUN chmod 755 /wpdl.sh  
ADD ./config/wp-config-musample.php /usr/share/nginx/www/wp-config-
musample.php  
ADD ./config/sunrise.php /usr/share/nginx/www/wp-content/sunrise.php  
  
# private expose  
EXPOSE 80  
# volume for mysql database and wordpress install  
VOLUME ["/usr/share/nginx/www/wp-content"]  
  
CMD ["/bin/bash", "/start.sh"]  
  
RUN date  

