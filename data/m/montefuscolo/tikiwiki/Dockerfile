FROM montefuscolo/php:5-apache  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
ARG
TIKI_SOURCE="https://gitlab.com/tikiwiki/tiki/-/archive/17.x/tiki-17.x.tar.gz"  
ARG TIKI_HTDOCS="/var/www/html"  
WORKDIR "${TIKI_HTDOCS}"  
  
RUN curl -o tiki.tar.gz -L "${TIKI_SOURCE}" \  
&& tar -C ${TIKI_HTDOCS} -zxf tiki.tar.gz --strip 1 \  
&& rm tiki.tar.gz \  
&& { \  
echo "<?php"; \  
echo " \$db_tiki = getenv('TIKI_DB_DRIVER') ?: 'mysqli';"; \  
echo " \$dbversion_tiki = getenv('TIKI_DB_VERSION') ?: '17';"; \  
echo " \$host_tiki = getenv('TIKI_DB_HOST') ?: 'db';"; \  
echo " \$user_tiki = getenv('TIKI_DB_USER');"; \  
echo " \$pass_tiki = getenv('TIKI_DB_PASS');"; \  
echo " \$dbs_tiki = getenv('TIKI_DB_NAME') ?: 'tikiwiki';"; \  
echo " \$client_charset = 'utf8';"; \  
} > ${TIKI_HTDOCS}/db/local.php \  
&& /bin/bash htaccess.sh \  
&& composer install --working-dir ${TIKI_HTDOCS}/vendor_bundled --prefer-dist
\  
&& chown -R root:root /var \  
&& find ${TIKI_HTDOCS} -type f -exec chmod 644 {} \; \  
&& find ${TIKI_HTDOCS} -type d -exec chmod 755 {} \; \  
&& chown -R www-data ${TIKI_HTDOCS}/db/ \  
&& chown -R www-data ${TIKI_HTDOCS}/dump/ \  
&& chown -R www-data ${TIKI_HTDOCS}/img/trackers/ \  
&& chown -R www-data ${TIKI_HTDOCS}/img/wiki/ \  
&& chown -R www-data ${TIKI_HTDOCS}/img/wiki_up/ \  
&& chown -R www-data ${TIKI_HTDOCS}/modules/cache/ \  
&& chown -R www-data ${TIKI_HTDOCS}/temp/ \  
&& chown -R www-data ${TIKI_HTDOCS}/temp/cache/ \  
&& chown -R www-data ${TIKI_HTDOCS}/temp/templates_c/ \  
&& chown -R www-data ${TIKI_HTDOCS}/templates/ \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
VOLUME [ \  
"${TIKI_HTDOCS}/files/", \  
"${TIKI_HTDOCS}/img/wiki/", \  
"${TIKI_HTDOCS}/img/wiki_up/", \  
"${TIKI_HTDOCS}/img/trackers/" \  
]  
  
EXPOSE 80 443  
CMD ["apache2-foreground"]  

