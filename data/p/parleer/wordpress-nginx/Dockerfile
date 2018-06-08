FROM ubuntu:trusty  
MAINTAINER Ryan Palree <parleer>  
  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# According to Dockerfile Best Practies, 'apt-get update' should NOT be run on
a single line and 'apt-get upgrade' should be avoided altogether.  
# However, I'm not sure yet how to do this correctly.  
RUN apt-get update  
#RUN apt-get -y upgrade  
# Wordpress Requirements  
RUN apt-get -y install nginx  
RUN apt-get -y install php5-fpm php5-mysql php-apc pwgen python-setuptools
curl git unzip  
  
# Wordpress Requirements  
RUN apt-get -y install php5-curl php5-gd php5-intl php-pear php5-imagick
php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode
php5-sqlite php5-tidy php5-xmlrpc php5-xsl  
  
# nginx config  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf  
RUN find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# nginx site conf  
ADD ./nginx-site.conf /etc/nginx/sites-available/default  
  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Install Wordpress  
RUN git clone \--depth=1 https://github.com/WordPress/WordPress.git /var/app  
RUN mv /usr/share/nginx/html/5* /var/app  
RUN chown -R www-data:www-data /var/app  
  
# Wordpress Initialization and Startup Script  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
#ADD sites-enabled/ /etc/nginx/sites-enabled/  
#ADD app/ /var/app/  
# prviate expose  
EXPOSE 80  
# volume wordpress install  
#VOLUME ["/var/lib/mysql"]  
VOLUME ["/var/app"]  
  
CMD ["/bin/bash", "/start.sh"]  
#CMD ["/usr/sbin/nginx"]  

