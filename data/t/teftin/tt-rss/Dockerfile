FROM debian:wheezy  
MAINTAINER Stan <teftin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y php5 php5-cli php5-curl php5-gd php5-mysqlnd
php5-xcache php5-fpm nginx runit  
  
ADD https://tt-rss.org/gitlab/fox/tt-rss/repository/archive.tar.gz?ref=master
/opt/  
RUN cd /opt && tar xzf archive.tar.gz  
ADD config.php /opt/tt-rss.git/  
RUN chown -R www-data:www-data /opt/tt-rss.git/lock  
RUN chown -R www-data:www-data /opt/tt-rss.git/cache  
RUN chown -R www-data:www-data /opt/tt-rss.git/feed-icons  
  
RUN sed -i.bak -e '/daemonize/c\daemonize = no' /etc/php5/fpm/php-fpm.conf  
  
RUN rm /etc/nginx/sites-enabled/default  
ADD tt-rss.conf /etc/nginx/conf.d/  
  
ADD sv /opt/sv  
  
EXPOSE 80  
CMD exec runsvdir /opt/sv  

