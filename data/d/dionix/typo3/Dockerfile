FROM php:apache  
MAINTAINER daniel@dionix.at  
  
# Typo3 version to install  
ENV TYPO3_VERSION 7.6.10  
# Typo3 backend admin username  
ENV TYPO3_ADMIN_USER admin  
# Typo3 backend admin password  
ENV TYPO3_ADMIN_PASSWORD password  
# Typo3 site name  
ENV TYPO3_SITE_NAME Typo3  
  
# install required PHP extensions  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libxml2-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-install mysqli && \  
docker-php-ext-install soap && \  
docker-php-ext-install zip  
  
# configure PHP as sugggested by Typo3  
RUN echo "max_execution_time=240\n\  
max_input_vars=1500" > /usr/local/etc/php/conf.d/typo3.ini  
  
# install PHP composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# create the composer config  
RUN echo "{\n\  
\"repositories\": [\n\  
{\"type\": \"composer\", \"url\": \"http://composer.typo3.org/\"},\n\  
{\"type\": \"vcs\", \"url\":
\"https://github.com/helhum/typo3_console.git\"}\n\  
],\n\  
\"name\": \"typo3/cms-console-distribution\",\n\  
\"description\" : \"TYPO3 CMS Console Distribution\",\n\  
\"license\": \"GPL-2.0+\",\n\  
\"config\": {\n\  
\"vendor-dir\": \"Packages/Libraries\",\n\  
\"bin-dir\": \"bin\",\n\  
\"secure-http\": false\n\  
},\n\  
\"scripts\": {\n\  
\"post-update-cmd\":
\"Helhum\\\\\\\\Typo3Console\\\\\\\\Composer\\\\\\\\InstallerScripts::postUpdateAndInstall\",\n\  
\"post-install-cmd\":
\"Helhum\\\\\\\\Typo3Console\\\\\\\\Composer\\\\\\\\InstallerScripts::postUpdateAndInstall\"\n\  
},\n\  
\"require\": {\n\  
\"typo3/cms\": \"${TYPO3_VERSION}\",\n\  
\"helhum/typo3-console\": \"*\"\n\  
}\n\  
}" > /var/www/html/composer.json  
  
RUN cat /var/www/html/composer.json  
  
# install git client, will be needed by PHP composer  
RUN apt-get install -y git  
  
# install Typo3  
RUN cd /var/www/html && \  
composer install  
  
# install MariaDB  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server  
  
# start MariaDB and setup Typo3  
RUN /etc/init.d/mysql start && \  
cd /var/www/html && \  
./typo3cms install:setup --non-interactive \  
\--database-user-name="root" \  
\--database-host-name="127.0.0.1" \  
\--database-port="3306" \  
\--database-name="typo3" \  
\--admin-user-name="${TYPO3_ADMIN_USER}" \  
\--admin-password="${TYPO3_ADMIN_PASSWORD}" \  
\--site-name="${TYPO3_SITE_NAME}" && \  
./typo3cms cache:warmup && \  
./typo3cms database:updateschema "*.add,*.change"  
  
# fix the ownership of the web directory  
RUN chown -R www-data:www-data /var/www/html  
  
# copy the entrypoint script  
COPY entrypoint.sh /usr/local/sbin/  
# make the entrypoint script executeable  
RUN chmod a+x /usr/local/sbin/entrypoint.sh  
  
# expose Apache  
EXPOSE 80  
  
# run the entrypoint script  
CMD ["entrypoint.sh"]  

