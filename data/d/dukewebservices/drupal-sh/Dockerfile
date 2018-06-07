FROM dukewebservices/php:7.0  
ENV DRUSH8_VER="8.1.10"  
ENV DRUSH7_VER="7.4.0"  
ENV DRUSH_BIN "drush8"  
ENV DRUPAL_CONSOLE_BIN "/opt/drupal.phar"  
RUN apk update \  
&& apk add mysql-client \  
&& apk add git \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt  
  
RUN wget https://github.com/drush-ops/drush/archive/${DRUSH7_VER}.tar.gz \  
&& tar -xzf ${DRUSH7_VER}.tar.gz \  
&& mv drush-${DRUSH7_VER} /opt \  
&& rm ${DRUSH7_VER}.tar.gz  
  
RUN cd /opt/drush-${DRUSH7_VER} && /opt/composer.phar install  
  
RUN wget https://github.com/drush-
ops/drush/releases/download/${DRUSH8_VER}/drush.phar -O /opt/drush.phar  
RUN chmod +x /opt/drush.phar  
  
RUN php -r "readfile('https://drupalconsole.com/installer');" > drupal.phar \  
&& chmod +x drupal.phar \  
&& mv drupal.phar /opt/drupal.phar \  
&& /opt/drupal.phar self-update  
  
RUN ln -s /opt/drush-${DRUSH7_VER}/drush /usr/local/bin/drush7  
RUN ln -s /opt/drush.phar /usr/local/bin/drush8  
  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["/bin/sh"]  

