FROM php:7.1-fpm  
MAINTAINER gan068<bleedkaga.ogre@gmail.com>  
  
ENV TZ=Asia/Taipei  
ADD ./*.zip /opt/oracle/  
ADD ./vim/.vimrc /root/.vimrc  
ADD ./vim/.vim/colors/* /root/.vim/colors/  
ADD ./fonts/*.ttc /usr/share/fonts/  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
libxrender1 \  
libfontconfig1 \  
git \  
vim \  
unzip \  
libaio1 \  
libaio-dev \  
freetds-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mysqli pdo_mysql soap zip
sockets fileinfo exif\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& sed -i "12a tds version = 8.0" /etc/freetds/freetds.conf  
  
WORKDIR /root  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-
setup.php');";php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;";php composer-setup.php;php -r
"unlink('composer-setup.php');";  
RUN unzip /opt/oracle/oracle-instantclient11.2-basic-11.2.0.1.0-1.x86_64.zip
-d /opt/oracle \  
&& unzip /opt/oracle/oracle-instantclient11.2-sdk-11.2.0.1.0-1.x86_64.zip -d
/opt/oracle \  
&& ln -s /opt/oracle/instantclient_11_2/libclntsh.so.11.1
/opt/oracle/instantclient_11_2/libclntsh.so \  
&& ln -s /opt/oracle/instantclient_11_2/libocci.so.11.1
/opt/oracle/instantclient_11_2/libocci.so \  
&& rm -rf /opt/oracle/*.zip \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so.5 /usr/lib/libsybdb.a \  
&& export ORACLE_HOME=/opt/oracle/instantclient_11_2 \  
&& export TNS_ADMIN=$ORACLE_HOME \  
&& export LD_LIBRARY_PATH=$ORACLE_HOME:/usr/local/lib:${LD_LIBRARY_PATH} \  
&& export SQLPATH=$ORACLE_HOME \  
&& export PATH=$PATH:$ORACLE_HOME  
RUN docker-php-ext-configure pdo_oci --with-pdo-
oci=instantclient,/opt/oracle/instantclient_11_2,11.2 \  
&& echo 'instantclient,/opt/oracle/instantclient_11_2/' | pecl install oci8 \  
&& docker-php-ext-install \  
pdo_oci \  
pdo_dblib \  
&& docker-php-ext-enable \  
oci8  
WORKDIR /var/www/html  

