################################################################################  
# Base image  
################################################################################  
  
FROM noriaas/composer:latest  
  
MAINTAINER Billy Nguyen <billy.nguyen@noria.no>  
  
################################################################################  
# Build instructions  
################################################################################  
  
ENV HOME /root  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
ENV JMETER_VERSON 3.3  
ENV JMETER_HOME=/noria/apache-jmeter-$JMETER_VERSON  
ENV PATH=$JMETER_HOME/bin:$PATH  
  
# Install packages  
RUN \  
set -ex; \  
apk add --no-cache --virtual .build-deps libxml2-dev wget; \  
apk add --no-cache --virtual .run-deps \  
libxml2 \  
graphviz \  
openjdk8-jre; \  
  
docker-php-ext-install xml; \  
export USE_CUSTOM_REPO=1; \  
/docker-entrypoint.sh global require --prefer-stable --prefer-dist \  
"squizlabs/php_codesniffer:3.*" \  
"phpunit/phpunit:6.*" \  
"phploc/phploc:4.*" \  
"pdepend/pdepend:^2.5" \  
"phpmd/phpmd:2.*" \  
"sebastian/phpcpd:2.*" \  
"friendsofphp/php-cs-fixer:2.*" \  
"phpmetrics/phpmetrics:2.*" \  
"clue/graph-composer:1.*"; \  
  
#Install Jmeter  
mkdir /noria; \  
wget -O - http://mirrors.viethosting.com/apache//jmeter/binaries/apache-
jmeter-${JMETER_VERSON}.tgz --progress=bar --tries=3 | tar xzf - -C /noria; \  
#Clean up  
apk del .build-deps; \  
rm -Rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apk/*; \  
  
#Default setting  
phpcs --config-set encoding utf-8; \  
phpcs --config-set tab_width 4; \  
phpcs --config-set default_standard Noria; \  
phpcs --config-set report_width 120; \  
mkdir /composer/vendor/squizlabs/php_codesniffer/src/Standards/Noria;  
  
COPY ./docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/douglascrockford/JSLint/master/jslint.js
./phpcs.xml ./phpmd.xml /phpqa/  
COPY ./phpcs.xml
/composer/vendor/squizlabs/php_codesniffer/src/Standards/Noria/ruleset.xml  
  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]

