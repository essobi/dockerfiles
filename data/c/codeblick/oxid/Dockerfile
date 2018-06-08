FROM codeblick/oxid:5.6-apache  
  
# install odbc driver  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \  
unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc  
  
ADD etc_odbcinst.ini /etc/odbcinst.ini  
  
# install odbc for php  
RUN set -ex; \  
docker-php-source extract; \  
{ \  
echo '# https://github.com/docker-
library/php/issues/103#issuecomment-271413933'; \  
echo 'AC_DEFUN([PHP_ALWAYS_SHARED],[])dnl'; \  
echo; \  
cat /usr/src/php/ext/odbc/config.m4; \  
} > temp.m4; \  
mv temp.m4 /usr/src/php/ext/odbc/config.m4; \  
docker-php-ext-configure odbc --with-unixODBC=shared,/usr; \  
docker-php-ext-install odbc; \  
docker-php-source delete  

