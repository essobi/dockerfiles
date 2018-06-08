# vim: set tabstop=4 shiftwidth=4 expandtab :  
# Writing Guidelines:  
# * https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/  
# * http://docs.projectatomic.io/container-best-practices/#  
FROM drupal:8.3-fpm  
  
LABEL name="plainlychrist/site-web" \  
version="1.0"  
  
MAINTAINER Jonah.Beckford@plainlychrist.org  
  
WORKDIR /var/www/html  
  
############# Versions  
# NGINX: https://hub.docker.com/_/nginx/ 1.13.3  
# DRUPAL_SECURITY_REVIEW: as of 9/8/2016, is a dev dependency
(https://packagist.drupal-
composer.org/packages/drupal/security_review#dev-8.x-1.x), which needs 'git
clone'  
# NPS: https://developers.google.com/speed/pagespeed/module/release_notes  
ENV NGINX_VERSION="1.13.3-1~jessie" \  
DRUSH_MAJOR_VERSION="8" \  
VIDEO_EMBED_FIELD_VERSION="^1.5" \  
DRUPAL_WORKBENCH_MODERATION_VERSION="^1.2" \  
DRUPAL_BACKUP_DB_VERSION="^1.2" \  
DRUPAL_ADVAGG_VERSION="^3.2" \  
DRUPAL_BOOTSTRAP_VERSION="^3.5" \  
MYSQL2SQLITE_VERSION="1b0b5d610c6090422625a2c58d2c23d2296eab3a" \  
DRUPAL_SECURITY_REVIEW_VERSION="^1.3" \  
NPS_VERSION="1.12.34.2" \  
NPS_STREAM="stable"  
########################  
######## ROOT ##########  
########################  
############## APT  
# Install gawk so mysql2sqlite does not Segfault on large bootstrap databases  
# Install git so that Composer, when fetching dev dependencies, can do a 'git
clone'  
# Install a database client, which is used by 'drush up' and 'drush sql-dump'  
# mysql-client or sqlite3  
# Install ruby and ruby-dev for 'gem install sass'  
# Install self-signed SSL (auto-generated) for HTTPS  
# Install supervisor so we can run multiple processes in one container  
RUN apt-get -y update && \  
apt-get -y install \  
gawk \  
git \  
mysql-client \  
ruby ruby-dev \  
sqlite3 \  
ssl-cert openssl-blacklist \  
supervisor && \  
gem install sass  
  
############## Nginx 1.13.5  
# - skips installing nginx-module-*  
# - skips remove /var/lib/apt/lists/*  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
gettext-base  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
# Install Google Page Speed Module for nginx  
#
https://developers.google.com/speed/pagespeed/module/build_ngx_pagespeed_from_source  
##########  
RUN apt-get install --no-install-recommends --no-install-suggests -y build-
essential zlib1g-dev libpcre3 libpcre3-dev unzip libssl-dev  
RUN set -x \  
&& cd \  
&& NGINX_VERSION=$(nginx -v 2>&1 | sed 's#.*/##') \  
&& PS_NGX_EXTRA_FLAGS=$(nginx -V 2>&1 | awk '/configure arguments:/{$1="";
$2=""; print}') \  
&& curl -LO
https://github.com/pagespeed/ngx_pagespeed/archive/v${NPS_VERSION}-${NPS_STREAM}.zip
\  
&& unzip v${NPS_VERSION}-${NPS_STREAM}.zip \  
&& cd ngx_pagespeed-${NPS_VERSION}-${NPS_STREAM}/ \  
&& psol_url=https://dl.google.com/dl/page-
speed/psol/${NPS_VERSION}-${NPS_STREAM}.tar.gz \  
&& [ -e scripts/format_binary_url.sh ] &&
psol_url=$(scripts/format_binary_url.sh PSOL_BINARY_URL) \  
&& curl -LO ${psol_url} \  
&& echo curl -LO https://dl.google.com/dl/page-
speed/psol/${NPS_VERSION}.tar.gz \  
&& echo tar -xzvf ${NPS_VERSION}.tar.gz \  
&& tar -xzvf $(basename ${psol_url}) \  
&& cd \  
&& curl -LO http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xvzf nginx-${NGINX_VERSION}.tar.gz \  
&& cd nginx-${NGINX_VERSION}/ \  
&& echo ./configure --add-dynamic-
module=$HOME/ngx_pagespeed-${NPS_VERSION}-${NPS_STREAM} $PS_NGX_EXTRA_FLAGS >
/tmp/runit \  
&& sh /tmp/runit \  
&& rm /tmp/runit \  
&& make \  
&& install -pv ./objs/ngx_pagespeed.so /etc/nginx/modules/ \  
&& cd \  
&& rm -rf release-${NPS_VERSION}-${NPS_STREAM}.zip ngx_pagespeed-
release-${NPS_VERSION}-${NPS_STREAM}/ nginx-${NGINX_VERSION}.tar.gz
nginx-${NGINX_VERSION}/ \  
&& apt-get remove -y build-essential zlib1g-dev libpcre3-dev unzip  
  
# Clean up space and unneeded packages  
##########  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Get rid of PHP extensions we don't need  
##########  
# We won't use: PostgreSQL (comes from Drupal Dockerfile)  
RUN rm -f /usr/local/etc/php/conf.d/docker-php-ext-pdo_pgsql.ini  
  
########################  
###### DRUPALADMIN #####  
########################  
# POSIX permissions: https://www.drupal.org/node/244924  
# Keep uid and gid stable across all Docker containers by setting to 200  
RUN addgroup --system --gid 200 drupaladmin  
RUN adduser --system --uid 200 --ingroup drupaladmin --shell /bin/false
drupaladmin  
  
# Give it the permissions it needs  
RUN chown -R drupaladmin \  
/var/www/html/composer.json \  
/var/www/html/composer.lock \  
/var/www/html/modules \  
/var/www/html/profiles \  
/var/www/html/themes \  
/var/www/html/vendor  
RUN chmod o+w \  
/var/www/html/modules \  
/var/www/html/profiles \  
/var/www/html/themes \  
/var/www/html/vendor  
  
# Switch to drupaladmin  
USER drupaladmin  
  
############# Composer  
# Install Composer with the phar file.  
RUN install -d ~/bin  
RUN curl -fsSL "https://getcomposer.org/installer" | php -- --install-dir
~/bin --filename=composer && \  
chmod +x ~/bin/composer  
  
# Choose where to install packages from  
RUN ~/bin/composer config repositories.drupal composer
https://packages.drupal.org/8  
  
############# Drush  
# Install Drush with Composer: http://www.whaaat.com/installing-drush-8-using-
composer  
RUN ~/bin/composer global require \  
drush/drush:${DRUSH_MAJOR_VERSION}.*  
RUN ln -s ~/.composer/vendor/bin/drush ~/bin/  
  
# Test your install.  
RUN ~/bin/drush core-status  
  
# Modules  
# To mitigate docker build running out of memory, we split up the composer
require commands  
#########  
# Video embedding (https://www.drupal.org/project/video_embed_field)  
# config_installer: Because of bug https://www.drupal.org/node/1613424, we
need this custom install profile  
RUN ~/bin/drush dl config_installer  
RUN ~/bin/composer require "drupal/video_embed_field
${VIDEO_EMBED_FIELD_VERSION}"  
  
# Install Backup and Migrate  
# Install Advanced CSS/JS Aggregation  
# Install security review  
# Install workbench moderation  
RUN ~/bin/composer require \  
"drupal/backup_db ${DRUPAL_BACKUP_DB_VERSION}" \  
"drupal/advagg ${DRUPAL_ADVAGG_VERSION}" \  
"drupal/security_review ${DRUPAL_SECURITY_REVIEW_VERSION}" \  
"drupal/workbench_moderation ${DRUPAL_WORKBENCH_MODERATION_VERSION}"  
  
# Install Bootstrap base theme  
RUN ~/bin/composer require \  
"drupal/bootstrap ${DRUPAL_BOOTSTRAP_VERSION}"  
  
# Install mysql2sqlite  
RUN curl
"https://raw.githubusercontent.com/dumblob/mysql2sqlite/${MYSQL2SQLITE_VERSION}/mysql2sqlite"
> ~/bin/mysql2sqlite && \  
chmod +x ~/bin/mysql2sqlite  
  
# Clean up drupaladmin  
##########  
RUN ~/bin/composer clear-cache  
  
########################  
######## ROOT ##########  
########################  
USER root  
  
# Configuration  
#########  
COPY filesystem/etc/ /etc/  
COPY filesystem/usr/local/etc/ /usr/local/etc/  
RUN rm -f /usr/local/etc/php-fpm.d/zz-docker.conf  
  
# Initial configuration for the 'all' site ...  
COPY filesystem/var/www/html/ /var/www/html  
RUN chown -R www-data:www-data /var/www/html/sites/all/modules
/var/www/html/sites/all/themes  
RUN chown www-data:www-data /var/www/html/*  
  
# Compile themes  
RUN install -o drupaladmin -g www-data -m 750 -d
/var/www/html/sites/all/themes/directjude/css && \  
sass \  
\--no-cache \  
\--default-encoding UTF-8 \  
/var/www/html/sites/all/themes/directjude/sass/style.scss \  
/var/www/html/sites/all/themes/directjude/css/style.css && \  
test -e /var/www/html/sites/all/themes/directjude/css/style.css  
  
# Clean up space and unneeded packages (we don't need SASS and hence Ruby
anymore)  
RUN gem cleanup all && \  
apt-get -y remove ruby && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Snippets used to build the settings.php and .htacess  
COPY settings/ /var/lib/site/settings  
  
# Installation  
############  
COPY filesystem/var/lib/site/ /var/lib/site/  
RUN chmod 500 /var/lib/site/bin/*.sh && \  
chown www-data /var/lib/site/bin/sanitized-backup.sh && \  
install -o drupaladmin -g www-data -m 750 -d /var/www/html/sites/default && \  
install -o drupaladmin -g www-data -m 770 -d /var/www/private && \  
chown -R drupaladmin:www-data /var/lib/site/storage-config/active  
  
ENTRYPOINT ["/var/lib/site/bin/entry.sh"]  

