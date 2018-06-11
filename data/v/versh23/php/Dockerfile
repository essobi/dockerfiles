FROM versh23/php:7.2  
  
# adding custom MS repository  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# install SQL Server drivers and tools  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql mssql-tools
php-pear php7.2-dev unixodbc-dev && \  
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile && \  
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \  
/bin/bash -c "source ~/.bashrc" && \  
pecl install pdo_sqlsrv && \  
apt-get remove mssql-tools php-pear php7.2-dev unixodbc-dev -y && apt-get
autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY php.ini /etc/php/7.2/cli/conf.d/50-mssql.ini  
COPY php.ini /etc/php/7.2/fpm/conf.d/50-mssql.ini

