FROM wordpress:apache  
  
# Install things  
RUN apt-get update && apt-get install -y \  
libjpeg-dev \  
libpng-dev \  
# libpng12-dev \  
# zlibc \  
# zlib1g \  
zlib1g-dev \  
mysql-client \  
wget \  
unzip \  
nano \  
sudo \  
less \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli zip opcache  
  
  
##############################################################################################  
# WORDPRESS CUSTOM SETUP  
##############################################################################################  
  
# Custom scripts  
# ADD vars.sh /vars.sh  
ADD ./entrypoint.sh /entrypoint.sh  
ADD ./plugins.sh /plugins.sh  
RUN chmod +x /entrypoint.sh /plugins.sh # /vars.sh  
  
# execute custom entrypoint script  
CMD ["/entrypoint.sh"]  
  
# Cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

