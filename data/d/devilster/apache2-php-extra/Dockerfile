ARG PHP_VER=5.6  
FROM devilster/apache2-php:${PHP_VER}  
  
LABEL maintainer="Devil.Ster.1"  
LABEL version="1.0"  
  
ARG PHP_VER  
  
# START PHP Additional Modules  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
\--allow-downgrades \--allow-remove-essential \--allow-change-held-packages \  
php$PHP_VER-pgsql \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# END PHP Additional Modules  
# START Additional Soft  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
\--allow-downgrades \--allow-remove-essential \--allow-change-held-packages \  
gcc \  
cmake \  
make \  
default-jre \  
postgresql-client \  
unzip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# END Additional Soft  
# START Install Redis Support For PHP  
RUN mkdir /tmp/phpredis && \  
cd /tmp/phpredis/ && \  
wget https://github.com/phpredis/phpredis/archive/3.1.6.zip -O phpredis.zip &&
\  
unzip -o ./phpredis.zip && \  
mv ./phpredis-* ./phpredis && \  
cd ./phpredis && \  
phpize && \  
./configure && \  
make && \  
make install && \  
echo "extension=redis.so" > /etc/php/${PHP_VER}/mods-available/redis.ini && \  
ln -s /etc/php/${PHP_VER}/mods-available/redis.ini
/etc/php/${PHP_VER}/apache2/conf.d/redis.ini && \  
ln -s /etc/php/${PHP_VER}/mods-available/redis.ini
/etc/php/${PHP_VER}/cli/conf.d/redis.ini && \  
rm -fr /tmp/phpredis  
# END Install Redis Support For PHP  
# START Install ZF1 Support  
RUN mkdir /tmp/zf1 && \  
cd /tmp/zf1 && \  
wget
https://github.com/zendframework/zf1/releases/download/release-1.12.20/ZendFramework-1.12.20-minimal.tar.gz
&& \  
tar -xvzf ZendFramework-1.12.20-minimal.tar.gz && \  
cp -R ZendFramework-1.12.20-minimal /usr/local/lib/ZendFramework1 && \  
sed -e 's/;include_path = ".:\/usr\/share\/php"/include_path =
".:\/usr\/local\/lib\/ZendFramework1\/library"/' -i
/etc/php/${PHP_VER}/apache2/php.ini && \  
rm -fr /tmp/zf1  
# END Install ZF1 Support  

