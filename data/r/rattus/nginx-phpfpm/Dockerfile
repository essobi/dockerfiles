FROM debian:jessie  
MAINTAINER Petr Vitek "rattus.PV@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list && \  
echo "deb-src http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list && \  
echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
echo '-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v2.0.22
(GNU/Linux)\n\nmQENBE5OMmIBCAD+FPYKGriGGf7NqwKfWC83cBV01gabgVWQmZbMcFzeW+hMsgxH\nW6iimD0RsfZ9oEbfJCPG0CRSZ7ppq5pKamYs2+EJ8Q2ysOFHHwpGrA2C8zyNAs4I\nQxnZZIbETgcSwFtDun0XiqPwPZgyuXVm9PAbLZRbfBzm8wR/3SWygqZBBLdQk5TE\nfDR+Eny/M1RVR4xClECONF9UBB2ejFdI1LD45APbP2hsN/piFByU1t7yK2gpFyRt\n97WzGHn9MV5/TL7AmRPM4pcr3JacmtCnxXeCZ8nLqedoSuHFuhwyDnlAbu8I16O5\nXRrfzhrHRJFM1JnIiGmzZi6zBvH0ItfyX6ttABEBAAG0KW5naW54IHNpZ25pbmcg\na2V5IDxzaWduaW5nLWtleUBuZ2lueC5jb20+iQE+BBMBAgAoAhsDBgsJCAcDAgYV\nCAIJCgsEFgIDAQIeAQIXgAUCV2K1+AUJGB4fQQAKCRCr9b2Ce9m/YloaB/9XGrol\nkocm7l/tsVjaBQCteXKuwsm4XhCuAQ6YAwA1L1UheGOG/aa2xJvrXE8X32tgcTjr\nKoYoXWcdxaFjlXGTt6jV85qRguUzvMOxxSEM2Dn115etN9piPl0Zz+4rkx8+2vJG\nF+eMlruPXg/zd88NvyLq5gGHEsFRBMVufYmHtNfcp4okC1klWiRIRSdp4QY1wdrN\n1O+/oCTl8Bzy6hcHjLIq3aoumcLxMjtBoclc/5OTioLDwSDfVx7rWyfRhcBzVbwD\noe/PD08AoAA6fxXvWjSxy+dGhEaXoTHjkCbz/l6NxrK3JFyauDgU4K4MytsZ1HDi\nMgMW8hZXxszoICTTiQEcBBABAgAGBQJOTkelAAoJEKZP1bF62zmo79oH/1XDb29S\nYtWp+MTJTPFEwlWRiyRuDXy3wBd/BpwBRIWfWzMs1gnCjNjk0EVBVGa2grvy9Jtx\nJKMd6l/PWXVucSt+U/+GO8rBkw14SdhqxaS2l14v6gyMeUrSbY3XfToGfwHC4sa/\nThn8X4jFaQ2XN5dAIzJGU1s5JA0tjEzUwCnmrKmyMlXZaoQVrmORGjCuH0I0aAFk\nRS0UtnB9HPpxhGVbs24xXZQnZDNbUQeulFxS4uP3OLDBAeCHl+v4t/uotIad8v6J\nSO93vc1evIje6lguE81HHmJn9noxPItvOvSMb2yPsE8mH4cJHRTFNSEhPW6ghmlf\nWa9ZwiVX5igxcvaIRgQQEQIABgUCTk5b0gAKCRDs8OkLLBcgg1G+AKCnacLb/+W6\ncflirUIExgZdUJqoogCeNPVwXiHEIVqithAM1pdY/gcaQZmIRgQQEQIABgUCTk5f\nYQAKCRCpN2E5pSTFPnNWAJ9gUozyiS+9jf2rJvqmJSeWuCgVRwCcCUFhXRCpQO2Y\nVa3l3WuB+rgKjsQ=\n=EWWI\n
-----END PGP PUBLIC KEY BLOCK-----\n' | sed 's/\\\n/\n/g' | apt-key add -  
  
# Basic packages + cleanup  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
locales \  
nginx \  
php5-cli \  
php5-common \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-imagick \  
php5-imap \  
php5-json \  
php5-mcrypt \  
php5-memcache \  
php5-pgsql \  
php5-sqlite \  
supervisor \  
cron && \  
apt-get install -y --no-install-recommends certbot -t jessie-backports && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && \  
chmod +x /usr/sbin/policy-rc.d  
  
# Ensure UTF-8  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# needed only for mysql  
#RUN php5enmod mcrypt  
# download and install composer  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates && \  
rm -rf /var/lib/apt/lists/* && \  
/usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php --
--install-dir=/usr/local/bin --filename=composer && \  
apt-get purge -y  
  
# Copy nginx and supervisor configuration  
COPY ./config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./config/nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY ./config/nginx/nette.conf /etc/nginx/nette.conf  
COPY ./config/nginx/realip.conf /etc/nginx/conf.d/realip.conf  
COPY ./config/supervisor.conf /etc/supervisor/conf.d/supervisord-nginx.conf  
COPY ./scripts/createSSLFiles.sh /opt/createSSLFiles.sh  
COPY ./config/certbot/certbot.cron /etc/cron.d/certbot  
COPY ./config/certbot/cli.ini /etc/letsencrypt/cli.ini  
  
# PHP-FPM config  
RUN mkdir -p /etc/nginx/ssl && \  
sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf  
  
# PHP  
COPY ./config/php/www.conf /etc/php5/fpm/pool.d/www.conf  
COPY ./config/php/php.ini /etc/php5/fpm/php.ini  
  
RUN mkdir -p /var/html/www && \  
usermod -u 1000 www-data && \  
chown -R www-data:www-data /var/html  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR /var/html  
  
#run supervisord with explicit config file  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord-
nginx.conf", "-n"]  

