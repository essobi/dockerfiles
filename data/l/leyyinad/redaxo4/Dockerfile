FROM php:7-apache  
ENV VERSION 4.7.2  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -yq apt-transport-https && \  
(curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -) && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
(curl -sL https://deb.nodesource.com/setup_6.x | bash -) && \  
apt-get install -yq \  
build-essential \  
imagemagick \  
libfreetype6-dev \  
libjpeg-dev \  
libpng-dev \  
libmcrypt-dev \  
mysql-client \  
nodejs \  
python \  
unzip \  
yarn \  
&& \  
docker-php-ext-configure gd --with-jpeg-dir=/usr --with-freetype-
dir=/usr/include/ && \  
docker-php-ext-install gd mysqli pdo pdo_mysql iconv mcrypt && \  
bash -c 'curl -SL
http://www.redaxo.org/de/download/file/?f=redaxo${VERSION//./_}.zip -o
/tmp/redaxo.zip' && \  
unzip /tmp/redaxo.zip -d /var/www/html && \  
chmod a+rw \  
/var/www/html/redaxo/include/master.inc.php \  
/var/www/html/redaxo/include/addons.inc.php \  
/var/www/html/redaxo/include/plugins.inc.php \  
/var/www/html/redaxo/include/clang.inc.php \  
/var/www/html/files/.redaxo && \  
chmod a+rwx \  
/var/www/html/redaxo/include/data \  
/var/www/html/redaxo/include/generated \  
/var/www/html/redaxo/include/generated/articles \  
/var/www/html/redaxo/include/generated/templates \  
/var/www/html/redaxo/include/generated/files \  
/var/www/html/files \  
/var/www/html/redaxo/include/addons \  
/var/www/html/redaxo/include/addons/import_export \  
/var/www/html/redaxo/include/addons/metainfo \  
/var/www/html/redaxo/include/addons/be_search \  
/var/www/html/redaxo/include/addons/image_manager \  
/var/www/html/redaxo/include/addons/install && \  
echo "\n\  
\$REX['DB']['1']['HOST'] = 'mysql';\n\  
\$REX['DB']['1']['LOGIN'] = 'root';\n\  
\$REX['DB']['1']['PSW'] = getenv('MYSQL_ENV_MYSQL_ROOT_PASSWORD');\n\  
\$REX['DB']['1']['NAME'] = getenv('MYSQL_ENV_MYSQL_DATABASE');\n\  
\$REX['DB']['1']['PERSISTENT'] = false; \n\  
\$REX['SETUP'] = false; \n\  
" >> /var/www/html/redaxo/include/master.inc.php && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

