FROM bettermood/php:latest  
  
#Install build packages and libaries  
ARG APTPACKAGES="unixodbc-dev"  
  
ARG APTLIBS="unixodbc"  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends $APTPACKAGES $APTLIBS  
  
  
# Install Microsoft depdencises for sqlsrv  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add \- \  
&& curl https://packages.microsoft.com/config/debian/8/prod.list -o
/etc/apt/sources.list.d/mssql-release.list \  
&& apt-get update \  
&& ACCEPT_EULA=Y apt-get install -y msodbcsql \  
&& pecl install sqlsrv-4.3.0 \  
&& docker-php-ext-enable sqlsrv  
  
# Keep our image size down..  
RUN pecl clear-cache \  
&& apt-get remove \--purge -y $APTPACKAGES \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*

