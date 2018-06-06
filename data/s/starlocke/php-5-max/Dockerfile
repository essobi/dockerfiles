FROM php:5-apache  
RUN apt-get update  
RUN docker-php-ext-install bcmath  
RUN apt-get install -y libbz2-dev  
RUN docker-php-ext-install bz2  
RUN docker-php-ext-install calendar  
RUN docker-php-ext-install ctype  
RUN apt-get install -y libcurl4-gnutls-dev  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install dba  
RUN apt-get install -y libxml2-dev  
RUN docker-php-ext-install dom  
RUN apt-get install -y libenchant-dev  
RUN docker-php-ext-install enchant  
RUN docker-php-ext-install exif  
RUN docker-php-ext-install fileinfo  
# RUN docker-php-ext-install filter  
RUN apt-get install -y libssl-dev  
RUN docker-php-ext-install ftp  
RUN apt-get install -y libpng-dev libjpeg-dev libgif-dev libxpm-dev  
RUN docker-php-ext-install gd  
RUN docker-php-ext-install gettext  
#RUN apt-get update  
#RUN apt-get install -y libgmp-dev  
#RUN docker-php-ext-install gmp  
RUN docker-php-ext-install hash  
RUN docker-php-ext-install iconv  
# RUN docker-php-ext-install imap  
# RUN docker-php-ext-install interbase  
RUN apt-get install -y libicu-dev  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install json  
RUN apt-get install -y libldap2-dev  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
RUN docker-php-ext-install mbstring  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
RUN apt-get install -y freetds-bin freetds-dev  
RUN ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/ && \  
docker-php-ext-install mssql  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-install mysqli  
# RUN docker-php-ext-install oci8  
# RUN docker-php-ext-install odbc  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install pcntl  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_dblib  
# RUN docker-php-ext-install pdo_firebird  
RUN docker-php-ext-install pdo_mysql  
# RUN docker-php-ext-install pdo_oci  
# RUN docker-php-ext-install pdo_odbc  
RUN apt-get install -y libpq-dev  
RUN docker-php-ext-install pdo_pgsql  
RUN apt-get install -y libsqlite3-dev  
RUN docker-php-ext-install pdo_sqlite  
RUN docker-php-ext-install pgsql  
RUN docker-php-ext-install phar  
RUN docker-php-ext-install posix  
RUN apt-get install -y libpspell-dev  
RUN docker-php-ext-install pspell  
# RUN docker-php-ext-install readline  
RUN apt-get install -y librecode-dev  
RUN docker-php-ext-install recode  
# RUN docker-php-ext-install reflection  
RUN docker-php-ext-install session  
RUN docker-php-ext-install shmop  
RUN docker-php-ext-install simplexml  
# RUN docker-php-ext-install snmp  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install sockets  
# RUN docker-php-ext-install spl  
# RUN docker-php-ext-install standard  
# RUN docker-php-ext-install sybase_ct  
RUN docker-php-ext-install sysvmsg  
RUN docker-php-ext-install sysvsem  
RUN docker-php-ext-install sysvshm  
RUN apt-get install -y libtidy-dev  
RUN docker-php-ext-install tidy  
RUN docker-php-ext-install tokenizer  
RUN docker-php-ext-install wddx  
RUN docker-php-ext-install xml  
# RUN docker-php-ext-install xmlreader  
RUN docker-php-ext-install xmlrpc  
RUN docker-php-ext-install xmlwriter  
RUN apt-get install -y libxslt1-dev  
RUN docker-php-ext-install xsl  
RUN apt-get install -y libzip-dev  
RUN docker-php-ext-install zip  

