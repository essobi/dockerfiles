FROM tweyand/ubuntu:zesty  
MAINTAINER Tim Weyand <tim.weyand@klambt.de>  
  
#------------------------------------  
# Building Options (Default Values)  
#------------------------------------  
#ENV INSTALL_PHP7 1  
#ENV INSTALL_PAGESPEED 1  
#ENV INSTALL_COMPOSER 1  
#ENV INSTALL_BROTLI 1  
#ENV INSTALL_GEM 1  
#ENV USE_OPCACHE_OPTIMIZATION 1  
ENV WORKDIR /var/www/html  
#ENV LANGUAGE de_DE.UTF-8  
#ENV TIMEZONE Europe/Berlin  
#ENV DOWNLOAD_APP_BUILD_FROM 0  
#ENV DOWNLOAD_APP_RUN_FROM 0  
#ENV COPY_EMPTY_WWW  
#ENV SETUP_FOR_PRODUCTION 1  
#ENV KLAMBT_WEBSERVER_PRODUCTION 1  
  
WORKDIR /var/www  
  
# -------------------------  
# Copy Customization  
# -------------------------  
COPY ./conf/ /root/docker-conf/  
COPY ./scripts/* /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/klambt_docker*.sh \  
&& eval `klambt_docker_webserver_environment_default_values.sh` \  
&& klambt_docker_webserver_environment_configuration.sh \  
&& tweyand_docker_apt_install_packages.sh \  
&& chown -R www-data:www-data /var/www \  
&& chmod -R 750 /var/www \  
&& klambt_docker_webserver_install_php7.sh \  
&& klambt_docker_webserver_install_apache_brotli.sh \  
&& klambt_docker_webserver_install_pagespeed.sh \  
&& klambt_docker_webserver_install_gem.sh \  
# -------------------------  
# Setup Logs/Directorys  
# -------------------------  
&& tweyand_docker_apt_cleanup.sh \  
&& rm -rf /var/log/apache2/error.log \  
&& rm -rf /var/log/apache2/access.log \  
&& ln -s /dev/stderr /var/log/apache2/error.log \  
&& ln -s /dev/stderr /var/log/apache2/access.log \  
# -------------------------  
# Add Configuration  
# -------------------------  
&& echo "Listen 80" > /etc/apache2/ports.conf \  
&& cp /root/docker-conf/apache2/security.conf /etc/apache2/conf-
available/security.conf \  
&& cp /root/docker-conf/apache2/remoteip.conf /etc/apache2/conf-
available/remoteip.conf \  
&& cp /root/docker-conf/apache2/000-default.conf /etc/apache2/sites-
available/000-default.conf \  
# -------------------------  
# Apache2 Module Setup  
# -------------------------  
&& a2enconf remoteip \  
&& a2disconf localized-error-pages serve-cgi-bin \  
&& a2enmod rewrite headers proxy proxy_http proxy_ajp expires remoteip  
  
WORKDIR $WORKDIR  
  
EXPOSE 80  
ENTRYPOINT ["klambt_docker_webserver_setup_entrypoint.sh"]  
CMD [ "klambt_docker_webserver_apache2-foreground.sh" ]

