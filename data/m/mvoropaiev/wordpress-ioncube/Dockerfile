# based on official wordpress docker image:  
# https://hub.docker.com/_/wordpress/  
# base image  
FROM wordpress:4.5.2-fpm  
  
# install the php extensions we need  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y \  
ssmtp \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install \  
mbstring \  
zip  
  
# ioncube loader  
ENV IONCUBE_VER '5.1.2'  
ENV IONCUBE_SHA256
'dacf7351cb750e999a59c8167d8057a8d2ca72d2391b74444db1b251a76c2fba'  
RUN set -ex \  
&& mkdir /tmp/ioncube_install \  
&& cd /tmp/ioncube_install \  
&& php_ext_dir="$(php -i | grep extension_dir | head -n1 | awk '{print $3}')"
\  
&& curl -fSL -o ioncube.tar.gz \  
"http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64_${IONCUBE_VER}.tar.gz"
\  
&& echo "$IONCUBE_SHA256 ioncube.tar.gz" | sha256sum --check \  
&& tar zxf ioncube.tar.gz \  
&& mv ./ioncube/ioncube_loader_lin_5.6.so "${php_ext_dir}/" \  
&& rm -rf /tmp/ioncube_install \  
&& echo "zend_extension = $php_ext_dir/ioncube_loader_lin_5.6.so" \  
> /usr/local/etc/php/conf.d/00-ioncube.ini  
  
# install required plugins  
ENV WP_PLUGINS_URL 'https://downloads.wordpress.org/plugin'  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y \  
unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /usr/src/wordpress/wp-content/plugins \  
&& curl -fSL -o updraftplus.zip \  
"$WP_PLUGINS_URL/updraftplus.1.12.12.zip" \  
&& unzip *.zip \  
&& rm *.zip  

