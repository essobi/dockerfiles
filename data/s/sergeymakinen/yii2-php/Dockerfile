FROM sergeymakinen/yii2-php:base  
  
LABEL maintainer="sergey@makinen.ru"  
# PHP 7.2  
RUN apt-get update && apt-get install -y php7.2-cli php7.2-curl php7.2-gd
php7.2-intl php7.2-mbstring php7.2-phpdbg php7.2-xml php7.2-zip \  
php7.2-mysql php7.2-pgsql php7.2-sqlite3 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ls -la /usr/lib/php/  
# OCI  
RUN apt-get update && apt-get install -y php-pear php7.2-dev && pecl channel-
update pecl.php.net \  
&& mkdir $ORACLE_HOME/lib/sdk && ln -s
$ORACLE/include/oracle/$ORACLE_INSTANTCLIENT_MAJOR/client64
$ORACLE_HOME/lib/sdk/include \  
&& echo "instantclient,$ORACLE_HOME/lib" | pecl install oci8 \  
&& rm -rf $ORACLE_HOME/lib/sdk \  
&& TMP_DIR="$(mktemp -d)" && cd "$TMP_DIR" && apt-get source php7.2 \  
&& cd $(find . -name 'php7.2-*' -type d)/ext/pdo_oci && phpize && ./configure
&& make \  
&& mv modules/pdo_oci.so /usr/lib/php/20170718 \  
&& echo 'extension=/usr/lib/php/20170718/oci8.so' > /etc/php/7.2/mods-
available/oci8.ini \  
&& echo 'extension=/usr/lib/php/20170718/pdo_oci.so' > /etc/php/7.2/mods-
available/pdo_oci.ini \  
&& phpenmod oci8 pdo_oci \  
&& rm -rf "$TMP_DIR" \  
&& rm -rf /var/lib/apt/lists/* && apt-get purge -y \--auto-remove php-pear
php7.2-dev  
# sqlsrv  
RUN apt-get update && apt-get install -y php-pear php7.2-dev curl apt-
transport-https \  
unixodbc-dev locales \  
&& echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && locale-gen && pecl channel-
update pecl.php.net \  
&& curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& curl -L https://packages.microsoft.com/config/ubuntu/16.04/prod.list -o
/etc/apt/sources.list.d/microsoft.list \  
&& apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql \  
&& pecl install sqlsrv pdo_sqlsrv \  
&& echo 'extension=/usr/lib/php/20170718/sqlsrv.so' > /etc/php/7.2/mods-
available/sqlsrv.ini \  
&& echo 'extension=/usr/lib/php/20170718/pdo_sqlsrv.so' > /etc/php/7.2/mods-
available/pdo_sqlsrv.ini \  
&& phpenmod sqlsrv pdo_sqlsrv \  
&& rm -rf /var/lib/apt/lists/* && apt-get purge -y \--auto-remove php-pear
php7.2-dev curl apt-transport-https  

