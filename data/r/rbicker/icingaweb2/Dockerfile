FROM php:7.0-apache  
  
MAINTAINER Raphael Bicker  
  
ENV MYSQL_ICINGAWEB_DB icingaweb2  
ENV MYSQL_ICINGAWEB_USER icingaweb2  
ENV MYSQL_ICINGAWEB_PASSWORD icingaweb2  
  
ENV MYSQL_DIRECTOR_DB director  
ENV MYSQL_DIRECTOR_USER director  
ENV MYSQL_DIRECTOR_PASSWORD director  
  
ENV ADMIN_USER admin  
ENV ADMIN_PASSWORD admin  
  
ENV ICINGAWEB2_VERSION master  
ENV ICINGAWEB2_DIRECTOR_VERSION master  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update \  
&& apt-get -qqy upgrade \  
&& apt-get install -y git mysql-client sudo sshpass \  
zlib1g-dev libicu-dev g++ libpng12-dev libjpeg62-turbo-dev libfreetype6-dev
libldap2-dev libcurl4-openssl-dev  
  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install -j$(nproc) intl gd ldap gettext curl pdo pdo_mysql  
  
RUN a2enmod rewrite  
  
RUN addgroup --system icingaweb2 \  
&& usermod -a -G icingaweb2 www-data  
  
RUN git clone http://git.icinga.org/icingaweb2.git /usr/share/icingaweb2 \  
&& git -C /usr/share/icingaweb2 checkout $ICINGAWEB2_VERSION \  
&& git clone http://github.com/Icinga/icingaweb2-module-director.git
/usr/share/icingaweb2/modules/director \  
&& git -C /usr/share/icingaweb2/modules/director checkout
$ICINGAWEB2_DIRECTOR_VERSION  
  
RUN /usr/share/icingaweb2/bin/icingacli setup config directory  
  
RUN mkdir -p /etc/icingaweb2/modules/monitoring \  
&& mkdir -p /etc/icingaweb2/modules/director  
  
RUN /usr/share/icingaweb2/bin/icingacli setup config webserver apache
--document-root /usr/share/icingaweb2/public > /etc/apache2/conf-
available/icingaweb2.conf \  
&& a2enconf icingaweb2 \  
&& echo "RedirectMatch ^/$ /icingaweb2/" >> /etc/apache2/apache2.conf  
  
RUN curl -L -o /usr/local/bin/jq
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \  
&& chmod +x /usr/local/bin/jq  
  
RUN mkdir -p /var/www/.ssh \  
&& chown www-data:www-data /var/www/.ssh \  
&& sudo -u www-data ssh-keygen -t rsa -N "" -f /var/www/.ssh/id_rsa  
  
ADD content/tmp/DbConnection.php.patch /tmp/DbConnection.php.patch  
ADD content/usr /usr  
ADD content/run.sh /run.sh  
  
# Fixing https://dev.icinga.org/issues/11264 /
https://dev.icinga.org/issues/11393, may probably be removed later  
# RUN chmod 1777 /tmp && patch -d /usr/share/icingaweb2/library/Icinga/Data/Db
< /tmp/DbConnection.php.patch  
RUN chmod +x /run.sh  
  
VOLUME ["/etc/icingaweb2"]  
  
EXPOSE 80 443  
CMD ["/run.sh"]  

