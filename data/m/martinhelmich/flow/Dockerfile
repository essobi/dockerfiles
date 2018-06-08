FROM ubuntu:15.04  
ENV FLOW_CONTEXT Production  
  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN apt-get install -y php5-fpm php5-mcrypt php5-mysqlnd php5-curl php5-gd
php5-json php5-xsl php5-cli php5-imagick  
RUN apt-get install -y supervisor  
  
RUN useradd -d /var/www flow  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \  
echo "date.timezone = Europe/Berlin" >> /etc/php5/fpm/php.ini && \  
echo "date.timezone = Europe/Berlin" >> /etc/php5/cli/php.ini && \  
echo "display_errors = off" >> /etc/php5/fpm/php.ini  
  
ADD fpm.conf /etc/php5/fpm/pool.d/www.conf  
ADD nginx-site.conf /etc/nginx/sites-enabled/default  
ADD supervisord.conf /etc/supervisor/conf.d/flow.conf  
ADD start.sh /opt/start.sh  
  
WORKDIR /var/www  
  
VOLUME /var/www/Data/Persistent  
EXPOSE 80  
ONBUILD ADD . /var/www  
ONBUILD RUN rm -rf /var/www/Data/Temporary  
ONBUILD VOLUME /var/www/Data/Temporary  
ONBUILD RUN chown -R flow.flow /var/www  
  
CMD ["/opt/start.sh"]  

