# Selene PHP Framework  
# Team: Dev  
# Author: Giovann Adonis <giovann@rsaweb.co.za>  
FROM ubuntu:14.04  
RUN sed -i -e 's/archive./de.archive./g' /etc/apt/sources.list  
  
RUN apt-get update  
  
RUN apt-get -y install libyaml-dev libyaml-0-2 libyaml-dev python python-dev
libmysqlclient-dev python-pip libmysqlclient-dev mysql-client libxslt1-dev
memcached php5 php5-mysql php-pear php5-curl php5-gd uuid-dev  
  
RUN apt-get -y install php5-cli nginx php5-fpm memcached libxrender-dev
libxext-dev  
  
RUN apt-get -y install php5-dev  
  
RUN pecl install memcache yaml uuid  
  
RUN touch /etc/rsaweb  
RUN echo "RSAWEB ISP" > /etc/rsaweb  
RUN echo "Date: 2016-07-02" >> /etc/rsaweb  
RUN echo "Selene PHP Framework" >> /etc/rsaweb  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN echo "extension=uuid.so" > /etc/php5/fpm/conf.d/uuid.ini && \  
echo "extension=yaml.so" > /etc/php5/fpm/conf.d/yaml.ini && \  
echo "extension=memcache.so" > /etc/php5/fpm/conf.d/memcache.ini && \  
echo "extension=uuid.so" > /etc/php5/cli/conf.d/uuid.ini && \  
echo "extension=yaml.so" > /etc/php5/cli/conf.d/yaml.ini && \  
echo "extension=memcache.so" > /etc/php5/cli/conf.d/memcache.ini  
  
RUN rm -rf /usr/share/nginx/html  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  
WORKDIR /usr/share/nginx/html  
  
# Define default command.  
CMD ["/usr/sbin/php5-fpm", "-F"]  
  

