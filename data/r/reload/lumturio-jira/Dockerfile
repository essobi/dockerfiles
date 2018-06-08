FROM composer AS build-env  
RUN echo "phar.readonly=false" > "$PHP_INI_DIR/conf.d/phar-not-readonly.ini"  
RUN composer global require kherge/box --prefer-dist --update-no-dev  
  
COPY . /opt/lumturio-jira/  
  
RUN cd /opt/lumturio-jira && composer install --prefer-dist --no-dev  
RUN cd /opt/lumturio-jira && /tmp/vendor/bin/box build -v --no-interaction  
  
FROM php:7.1-alpine  
  
COPY \--from=build-env /opt/lumturio-jira/lumturio-jira.phar /opt/lumturio-
jira/lumturio-jira.phar  
  
RUN apk add --update tini && rm -rf /var/cache/apk/*  
  
RUN crontab -l | { cat; echo '*/10 * * * * eval $(printenv | grep -E
"^(JIRA|LUMTURIO)_" | sed "s/^\\(.*\\)$/export \1/g"); /opt/lumturio-
jira/lumturio-jira.phar --verbose'; } | crontab -  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/usr/sbin/crond", "-f"]  

