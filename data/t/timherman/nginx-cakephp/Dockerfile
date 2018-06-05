FROM ubuntu:latest  
MAINTAINER Tim Herman <tim@belg.be>  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Basic Requirements  
RUN apt-get -y install nginx php5-fpm php5-mysql php-apc pwgen python-
setuptools curl git ssmtp  
  
# Wordpress Requirements  
RUN apt-get -y install php5-curl php5-gd php5-intl php-pear php5-imagick
php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode
php5-sqlite php5-tidy php5-xmlrpc php5-xsl  
  
# Wordpress Initialization and Startup Script  
ADD /scripts /scripts  
ADD /config /config  
RUN chmod 755 /scripts/*.sh  
  
# nginx config  
RUN cp /config/nginx/nginx.conf /etc/nginx/nginx.conf  
RUN cp /config/nginx/nginx-host.conf /etc/nginx/sites-available/default  
RUN cp /config/nginx/apc.ini /etc/php5/mods-available/apcu.ini  
  
# php-fpm config  
RUN cp /config/nginx/php.ini /etc/php5/fpm/php.ini  
RUN cp /config/nginx/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
RUN cp /config/nginx/www.conf /etc/php5/fpm/pool.d/www.conf  
  
# Enabling session files  
RUN mkdir -p /tmp/sessions/  
RUN chown www-data.www-data /tmp/sessions -Rf  
RUN sed -i -e "s:;\s*session.save_path\s*=\s*\"N;/path\":session.save_path =
/tmp/sessions:g" /etc/php5/fpm/php.ini  
  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD /config/supervisor/supervisord.conf /etc/supervisord.conf  
  
VOLUME /var/www  
EXPOSE 80  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
CMD ["/bin/bash", "/scripts/start.sh"]  

