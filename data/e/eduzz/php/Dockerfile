FROM php:7.2-cli  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y libsybdb5 freetds-dev locales gnupg2 apt-transport-https
\  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/ \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& curl https://packages.microsoft.com/config/debian/9/prod.list | tee
/etc/apt/sources.list.d/mssql-release.list \  
&& apt-get update \  
&& ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev \  
&& docker-php-ext-install -j$(nproc) pdo_dblib bcmath \  
&& pecl install redis sqlsrv-5.2.0 pdo_sqlsrv-5.2.0 \  
&& docker-php-ext-enable redis sqlsrv pdo_sqlsrv \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY freetds.conf /etc/freetds/freetds.conf  

