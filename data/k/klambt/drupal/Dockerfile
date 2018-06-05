FROM klambt/webserver:latest  
MAINTAINER Tim Weyand <tim.weyand@klambt.de>  
  
ENV UPDATE_DEBIAN 1  
ENV INSTALL_DRUSH 1  
ENV INSTALL_DRUPAL 1  
ENV INSTALL_COMPOSER 1  
ENV MYSQL_DATABASE drupal  
ENV MYSQL_USER drupal  
ENV MYSQL_PASSWORD drupal  
ENV MYSQL_PORT 3306  
ENV MYSQL_LINK database_server  
ENV DRUPAL_USERNAME admin  
ENV DRUPAL_USER_PASSWORD 0  
ENV DRUPAL_USER_MAIL webmaster@domain.tld  
ENV DRUPAL_SITE_MAIL webmaster@domain.tld  
ENV DRUPAL_MEMCACHE_SERVER 0  
ENV DRUPAL_VARNISH_SERVER 0  
ENV DRUPAL_VARNISH_KEY xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx  
ENV DRUPAL_INSTALL_MODULES 0  
ENV DEBIAN_INSTALL_PACKAGES 0  
ENV GIT_PULL_CUSTOM 0  
ENV GIT_CUSTOM_SOURCES_SERVER github.com  
ENV GIT_CUSTOM_SOURCES_REPOS 0  
ENV GIT_USERNAME 0  
ENV GIT_PASSWORD 0  
ENV GIT_CUSTOM_MODULES_PATH 0  
ENV GIT_CUSTOM_THEMES_PATH 0  
COPY ./scripts/* /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/klambt_docker_*.sh \  
&& /usr/local/bin/klambt_docker_update_debian.sh \  
&& /usr/local/bin/klambt_docker_install_drush.sh \  
&& /usr/local/bin/klambt_docker_install_drupal.sh drupal-8 \  
  
# @todo customization  
CMD ["/usr/local/bin/klambt_docker_drupal_start-8.sh"]

