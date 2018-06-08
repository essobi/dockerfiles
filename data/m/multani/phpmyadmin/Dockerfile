FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
ca-certificates \  
libapache2-mod-php5 \  
php5-mysql \  
php5-redis \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm /etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*
/etc/apache2/apache2.conf  
RUN a2dismod mpm_event && a2enmod mpm_prefork  
  
ENV PHPMYADMIN_VERSION 4.6.2  
#
https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-all-
languages.tar.gz.sha1  
ENV PHPMYADMIN_SHA1 5d1b4a3f74ebfde3aafbdea0a04470a7e7811b8b  
  
RUN wget --quiet
https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-all-
languages.tar.gz -O /phpmyadmin.tar.gz \  
&& echo "${PHPMYADMIN_SHA1} /phpmyadmin.tar.gz" | sha1sum -c - \  
&& tar -xvf /phpmyadmin.tar.gz -C / \  
&& rm -rf /phpmyadmin.tar.gz /var/www/html \  
&& mv /phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages /var/www/html \  
&& rm -rf /var/www/html/setup \  
&& chown -R www-data:www-data /var/www/html  
  
COPY apache2.conf /etc/apache2/apache2.conf  
  
VOLUME ["/run", "/tmp"]  
  
CMD ["apache2", "-DFOREGROUND"]  

