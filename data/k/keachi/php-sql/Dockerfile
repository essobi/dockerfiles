FROM php:7.2-apache  
  
RUN echo "deb http://pkg.adfinis-sygroup.ch/debian/ jessie main contrib non-
free" \  
> /etc/apt/sources.list && \  
echo "deb http://security.debian.org/ jessie/updates main" \  
>> /etc/apt/sources.list && \  
echo "deb http://pkg.adfinis-sygroup.ch/debian/ jessie-updates main contrib
non-free" \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/*  
RUN docker-php-ext-install mysqli pdo pdo_mysql  

