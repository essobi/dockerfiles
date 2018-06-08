#
https://github.com/nextcloud/docker/blob/master/.examples/dockerfiles/full/apache/Dockerfile  
FROM nextcloud:13-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV CRON_MEMORY_LIMIT 1024M  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
supervisor \  
cron \  
libmagickwand-dev \  
libgmp3-dev \  
libc-client-dev libkrb5-dev \  
smbclient libsmbclient-dev \  
locales locales-all \  
&& apt-get install --no-install-recommends --no-install-suggests -y -t jessie-
backports ffmpeg \  
&& ln -s "/usr/include/$(dpkg-architecture --query DEB_BUILD_MULTIARCH)/gmp.h"
/usr/include/gmp.h \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl >/dev/null \  
&& docker-php-ext-install bz2 gmp imap >/dev/null \  
&& pecl install imagick smbclient >/dev/null \  
&& docker-php-ext-enable imagick smbclient \  
&& rm -f /etc/cron.*/* \  
&& echo "*/15 * * * * su - www-data -s /bin/bash -c \"/usr/local/bin/php -d
memory_limit=$CRON_MEMORY_LIMIT -f /var/www/html/cron.php\"" | crontab - \  
&& a2enmod rewrite headers env dir mime \  
&& a2dismod status \  
&& sed -i 's/^ServerSignature On/ServerSignature Off/' /etc/apache2/conf-
available/security.conf \  
&& sed -i 's/^ServerTokens OS/ServerTokens Minimal/' /etc/apache2/conf-
available/security.conf \  
&& echo 'Europe/Paris' > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get clean \  
&& dpkg -l | awk '{print $2}' | grep '\\-dev' | xargs apt-get remove --purge
-y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/* /usr/share/doc
/usr/share/man  
  
ENV TZ=Europe/Paris  
ENV LC_ALL fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR.UTF-8  
  
COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
# ATTENTION cette conf execute le script de l'image php:7.1-apache :
/usr/local/bin/apache2-foreground  
COPY supervisor/apache2-foreground.conf
/etc/supervisor/conf.d/apache2-foreground.conf  
COPY supervisor/cron.conf /etc/supervisor/conf.d/cron.conf  
  
HEALTHCHECK --interval=30s \--timeout=30s \--start-period=1s \--retries=3 CMD
curl -o /dev/null -sm 10 http://localhost/ || exit 1  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

