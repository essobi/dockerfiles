# many thanks to:  
# https://github.com/lazyfrosch/docker-icingaweb2  
  
FROM php:5.6-apache  
  
# set environment variables  
ENV ICINGAWEB_VERSION 2.4.2  
ENV ICINGADIRECTOR_VERSION 1.4.0  
#ENV ICINGAWEB_SETUP_TOKEN docker  
  
  
# install dependencies  
RUN apt-get update && apt-get install -y libicu-dev libldap2-dev libpng12-dev
libpq-dev libjpeg-dev php5-imagick python-pip git php5-curl && rm -rf
/var/lib/apt/lists/* \  
&& pip install j2cli \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd gettext intl ldap mysql pdo_mysql pdo_pgsql pgsql  
  
# download and extract icingaweb2  
RUN curl -o /tmp/icingaweb2.tar.gz -SL
"https://github.com/Icinga/icingaweb2/archive/v${ICINGAWEB_VERSION}.tar.gz" \  
&& mkdir /usr/share/icingaweb2 \  
&& tar xf /tmp/icingaweb2.tar.gz --strip-components=1 -C /usr/share/icingaweb2
\  
&& rm -f /tmp/icingaweb2.tar.gz \  
&& ln -s /usr/share/icingaweb2/bin/icingacli /usr/local/bin/icingacli  
  
# download icingaweb2 module: graphite  
RUN git clone https://github.com/findmypast/icingaweb2-module-graphite.git
/usr/share/icingaweb2/modules/graphite  
  
# download and extract icingaweb2 module: icinga director  
RUN curl -o /tmp/icingaweb2-module-director.tar.gz -SL
"https://github.com/Icinga/icingaweb2-module-
director/archive/v${ICINGADIRECTOR_VERSION}.tar.gz" \  
&& mkdir /usr/share/icingaweb2/modules/director \  
&& tar xf /tmp/icingaweb2-module-director.tar.gz --strip-components=1 -C
/usr/share/icingaweb2/modules/director \  
&& rm -f /tmp/icingaweb2-module-director.tar.gz  
  
  
  
# enable apache vHost  
RUN cp /usr/share/icingaweb2/packages/files/apache/icingaweb2.conf
/etc/apache2/conf-enabled/ \  
&& echo "RedirectMatch ^/$ /icingaweb2" >> /etc/apache2/conf-
enabled/redirect.conf \  
&& a2enmod rewrite \  
&& echo "date.timezone = UTC" > /usr/local/etc/php/conf.d/timeszone.ini  
  
  
#VOLUME /etc/icingaweb2  
  
  
# configure icingaweb2  
COPY files/etc/icingaweb2/authentication.ini.j2 /etc/icingaweb2/  
COPY files/etc/icingaweb2/config.ini.j2 /etc/icingaweb2/  
COPY files/etc/icingaweb2/groups.ini.j2 /etc/icingaweb2/  
COPY files/etc/icingaweb2/resources.ini.j2 /etc/icingaweb2/  
COPY files/etc/icingaweb2/roles.ini.j2 /etc/icingaweb2/  
  
COPY files/etc/icingaweb2/modules/monitoring/backends.ini.j2
/etc/icingaweb2/modules/monitoring/  
COPY files/etc/icingaweb2/modules/monitoring/commandtransports.ini.j2
/etc/icingaweb2/modules/monitoring/  
COPY files/etc/icingaweb2/modules/monitoring/config.ini.j2
/etc/icingaweb2/modules/monitoring/  
  
# configure icingaweb2 module: graphite  
COPY files/etc/icingaweb2/modules/graphite/config.ini.j2
/etc/icingaweb2/modules/graphite/  
  
# configure icingaweb2 module: director  
COPY files/etc/icingaweb2/modules/director/config.ini.j2
/etc/icingaweb2/modules/director/  
  
  
  
# enable modules  
RUN icingacli module enable monitoring  
RUN icingacli module enable graphite  
RUN icingacli module enable director  
  
  
# copy entrypoint  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
  
# start script  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "apache2-foreground" ]  

