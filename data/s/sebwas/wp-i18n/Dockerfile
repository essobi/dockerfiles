FROM php:7.1  
MAINTAINER Sebastian Wasser <sebastian.wasser@gmail.com>  
LABEL Maintainer Sebastian Wasser <sebastian.wasser@gmail.com>  
  
ENV WP_TARGET_DIR=${WP_TARGET_DIR:-/var/src}  
ENV ASSET_TARGET_DIR=${ASSET_TARGET_DIR:-/var/www/html}  
ENV I18N_TARGET_DIR=${I18N_TARGET_DIR:-/var/www/i18n}  
  
RUN mkdir -p $WP_TARGET_DIR && \  
mkdir -p $ASSET_TARGET_DIR && \  
mkdir -p $I18N_TARGET_DIR && \  
cd $WP_TARGET_DIR && \  
curl -O https://wordpress.org/latest.tar.gz && \  
tar --strip-components=1 -C $WP_TARGET_DIR -xzf latest.tar.gz wordpress/wp-
includes && \  
rm latest.tar.gz && \  
cd $I18N_TARGET_DIR && \  
curl -O https://develop.svn.wordpress.org/trunk/tools/i18n/makepot.php && \  
curl -O https://develop.svn.wordpress.org/trunk/tools/i18n/not-gettexted.php
&& \  
curl -O https://develop.svn.wordpress.org/trunk/tools/i18n/extract.php && \  
curl -O https://develop.svn.wordpress.org/trunk/tools/i18n/add-textdomain.php
&& \  
curl -O https://develop.svn.wordpress.org/trunk/tools/i18n/pot-ext-meta.php &&
\  
apt-get update && apt-get install -y gettext && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
WORKDIR $ASSET_TARGET_DIR  
  
COPY ./entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

