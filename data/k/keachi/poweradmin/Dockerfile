FROM php:7.1-apache-jessie  
  
ENV POWERADMIN_HOSTMASTER ""  
ENV POWERADMIN_NS1 8.8.8.8  
ENV POWERADMIN_NS2 8.8.4.4  
ENV DNS_TTL 86400  
ENV MYSQL_HOST localhost  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER pdns  
ENV MYSQL_PASS pdns  
ENV MYSQL_DB pdns  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
mariadb-client \  
libmcrypt-dev  
RUN docker-php-ext-install \  
mysqli \  
pdo \  
pdo_mysql \  
gettext \  
mcrypt  
RUN curl -L https://github.com/poweradmin/poweradmin/archive/v2.1.7.tar.gz >
/poweradmin.tar.gz \  
&& tar -xav -C /var/www -f /poweradmin.tar.gz \  
&& rm -rf /var/www/html \  
&& mv /var/www/poweradmin* /var/www/html \  
&& chown -R root:root /var/www/html  
RUN apt-get autoremove --purge -y \  
&& rm -rf /var/lib/apt/lists/* /poweradmin.tar.gz /var/www/html/install  
  
COPY assets/config.inc.php /var/www/html/inc/config.inc.php  
COPY assets/poweradmin.sql entrypoint.sh /  
  
ENTRYPOINT [ \  
"/bin/bash", \  
"/entrypoint.sh" \  
]  

