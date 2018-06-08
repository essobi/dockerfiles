############################################################  
# Dockerfile to build PHP  
# Based on php:7-fpm  
############################################################  
# Based image  
FROM php:7.0-fpm  
  
# Maintainer  
MAINTAINER shavene <shaveneLee@gmail.com>  
  
RUN apt-get clean -y  
RUN apt update  
RUN apt upgrade -y  
RUN apt install -y apt-utils  
RUN apt install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
RUN apt install -y libicu-dev  
RUN docker-php-ext-install -j$(nproc) intl  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
RUN apt install -y php-apc  
RUN apt install -y libxml2-dev  
RUN apt install -y libldb-dev  
RUN apt install -y libldap2-dev  
RUN apt install -y libxml2-dev  
RUN apt install -y libssl-dev  
RUN apt install -y libxslt-dev  
RUN apt install -y libpq-dev  
RUN apt install -y postgresql-client  
RUN apt install -y mysql-client  
RUN apt install -y libsqlite3-dev  
RUN apt install -y libsqlite3-0  
RUN apt install -y libc-client-dev  
RUN apt install -y libkrb5-dev  
RUN apt install -y curl  
RUN apt install -y libcurl3  
RUN apt install -y libcurl3-dev  
RUN apt install -y firebird-dev  
RUN apt-get install -y libpspell-dev  
RUN apt-get install -y aspell-en  
RUN apt-get install -y aspell-de  
RUN apt install -y libtidy-dev  
RUN apt install -y libsnmp-dev  
RUN apt install -y librecode0  
RUN apt install -y librecode-dev  
RUN docker-php-ext-install soap  
#RUN docker-php-ext-install ftp  
RUN docker-php-ext-install xsl  
#RUN docker-php-ext-install bcmath  
#RUN docker-php-ext-install calendar  
#RUN docker-php-ext-install ctype  
#RUN docker-php-ext-install dba  
#RUN docker-php-ext-install dom  
RUN docker-php-ext-install zip  
#RUN docker-php-ext-install session  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
RUN docker-php-ext-install ldap  
#RUN docker-php-ext-install json  
#RUN docker-php-ext-install hash  
RUN docker-php-ext-install sockets  
#RUN docker-php-ext-install pdo  
RUN docker-php-ext-install mbstring  
#RUN docker-php-ext-install tokenizer  
#RUN docker-php-ext-install pgsql  
#RUN docker-php-ext-install pdo_pgsql  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install pdo_sqlite  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
RUN docker-php-ext-install imap  
#RUN docker-php-ext-install gd  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install exif  
RUN docker-php-ext-install fileinfo  
RUN docker-php-ext-install gettext  
##RUN apt install -y libgmp-dev # idk  
##RUN docker-php-ext-install gmp # idk  
#RUN docker-php-ext-install iconv  
#RUN docker-php-ext-install interbase  
#RUN docker-php-ext-install pdo_firebird  
#RUN docker-php-ext-install opcache  
##RUN docker-php-ext-install oci8 # idk  
##RUN docker-php-ext-install odbc # idk  
#RUN docker-php-ext-install pcntl  
##RUN apt install -y freetds-dev # idk  
##RUN docker-php-ext-install pdo_dblib # idk  
##RUN docker-php-ext-install pdo_oci # idk  
##RUN docker-php-ext-install pdo_odbc # idk  
#RUN docker-php-ext-install phar  
#RUN docker-php-ext-install posix  
#RUN docker-php-ext-install pspell  
##RUN apt install -y libreadline-dev # idk  
##RUN docker-php-ext-install readline # idk  
#RUN docker-php-ext-install recode  
#RUN docker-php-ext-install shmop  
RUN docker-php-ext-install simplexml  
#RUN docker-php-ext-install sysvmsg  
#RUN docker-php-ext-install sysvsem  
#RUN docker-php-ext-install sysvshm  
#RUN docker-php-ext-install tidy  
#RUN docker-php-ext-install wddx  
#Install OCI8  
RUN mkdir -p /tmp/inst  
COPY ./oci8/instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/inst  
COPY ./oci8/instantclient-sdk-linux.x64-12.1.0.2.0.zip /tmp/inst  
COPY ./oci8/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip /tmp/inst  
RUN apt-get install -y unzip libaio-dev  
RUN unzip /tmp/inst/instantclient-basic-linux.x64-12.1.0.2.0.zip -d
/usr/local/  
RUN unzip /tmp/inst/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/  
RUN unzip /tmp/inst/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip -d
/usr/local/  
RUN rm -rf /tmp/inst  
  
RUN ln -s /usr/local/instantclient_12_1 /usr/local/instantclient  
RUN ln -s /usr/local/instantclient/libclntsh.so.12.1
/usr/local/instantclient/libclntsh.so  
RUN ln -s /usr/local/instantclient/sqlplus /usr/bin/sqlplus  
RUN docker-php-ext-configure oci8 --with-
oci8=instantclient,/usr/local/instantclient  
RUN docker-php-ext-install oci8  
  
#Install yar  
#RUN apt-get install -y wget tar  
#RUN wget https://pecl.php.net/get/yar-2.0.1.tgz -P /tmp  
#RUN tar -xvf /tmp/yar-2.0.1.tgz -C /usr/local/  
RUN curl -fsSL 'https://pecl.php.net/get/yar-2.0.1.tgz' -o yar.tar.gz \  
&& mkdir -p /tmp/yar \  
&& tar -xf yar.tar.gz -C /tmp/yar --strip-components=1 \  
&& rm yar.tar.gz \  
&& docker-php-ext-configure /tmp/yar --enable-yar \  
&& docker-php-ext-install /tmp/yar \  
&& rm -rf /tmp/yar  
  
#Install compress pkg  
RUN apt-get install -y tar  
RUN apt-get install -y zip  
RUN curl 'https://www.rarlab.com/rar/rarlinux-x64-5.5.0.tar.gz' -o
/tmp/rar.tar.gz \  
&& mkdir -p /tmp/rar \  
&& cd /tmp \  
&& rm -rf rar \  
&& tar -xvf rar.tar.gz \  
&& rm rar.tar.gz \  
&& cd rar \  
&& make \  
&& make install \  
&& rm -rf /tmp/rar  
RUN curl
'https://ncu.dl.sourceforge.net/project/p7zip/p7zip/16.02/p7zip_16.02_src_all.tar.bz2'
-o /tmp/7zip.tar.bz2 \  
&& cd /tmp \  
&& tar -jxvf 7zip.tar.bz2 \  
&& rm 7zip.tar.bz2 \  
&& cd p7zip_16.02 \  
&& make \  
&& make install \  
&& rm -f p7zip_16.02  
# install wkhtmltox  
RUN apt-get install -y rpm  
RUN mkdir -p /tmp/wk  
COPY ./wk/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb /tmp/wk  
RUN apt-get install -y fontconfig libx11-6  
RUN apt-get install -y libxext6 libxrender1 xfonts-base xfonts-75dpi  
RUN dpkg -i /tmp/wk/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb  
RUN rm -rf /tmp/wk  
  
# install rdkafka  
RUN mkdir -p /tmp/kafka  
RUN cd /tmp/kafka \  
rm -rf librdkafka-master  
RUN curl 'https://codeload.github.com/edenhill/librdkafka/zip/master' -o
librdkafka-master.zip \  
&& unzip librdkafka-master.zip \  
&& cd librdkafka-master \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig  
  
RUN cd /tmp/kafka  
RUN rm -rf php-rdkafka-master  
RUN curl 'https://codeload.github.com/arnaud-lb/php-rdkafka/zip/master' -o
phpkafka-master.zip \  
&& unzip phpkafka-master.zip \  
&& cd php-rdkafka-master \  
&& /usr/local/bin/phpize \  
&& ./configure --enable-kafka --with-php-config=/usr/local/bin/php-config \  
&& make \  
&& make install  
RUN docker-php-ext-enable rdkafka  

