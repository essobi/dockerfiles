# Build image with: docker build -t nanointeractive/testenv:latest .  
  
FROM amazonlinux:2017.09  
MAINTAINER Zeljko Nedeljkovic <znedeljkovic@nanointeractive.com>  
  
ADD selenium-server-standalone-2.46.0.jar /usr/local/lib/selenium-server-
standalone-2.46.0.jar  
ADD libs /tmp/libs  
ADD GeoIP.dat /usr/share/GeoIP/GeoIP.dat  
ADD GeoLiteCity.dat /usr/share/GeoIP/GeoLiteCity.dat  
  
RUN yum install -y php71 php71-devel php71-pdo php71-mysqlnd php7-pear
php71-bcmath php71-mbstring php71-soap php71-apc php71-opcache mod24_ssl &&\  
yum install -y python27-pip git curl wget &&\  
yum install -y java-1.8.0 &&\  
pip-2.7 install cqlsh &&\  
pear7 channel-discover guzzlephp.org/pear &&\  
pear7 channel-discover pear.symfony.com &&\  
pear7 install guzzle/Guzzle &&\  
cd /usr/local/bin/ &&\  
curl -L https://phar.phpunit.de/phpunit-6.4.phar > phpunit &&\  
chmod +x phpunit &&\  
chmod +X /usr/local/bin/cqlsh &&\  
export CQLSH_NO_BUNDLED=TRUE &&\  
sed -i "/DEFAULT_CQLVER = '/c\DEFAULT_CQLVER = '3.4.2'" /usr/local/bin/cqlsh
&&\  
ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime &&\  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer &&\  
ln -sf /usr/share/GeoIP/GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat &&\  
cd /tmp/libs &&\  
sh install.sh &&\  
cp /tmp/libs/php-7.1.ini /etc/php-7.1.ini &&\  
cp /tmp/libs/libphpcpp.so.2.0 /usr/lib64 &&\  
cp /tmp/libs/nanocookiebulkuploader.so /usr/lib64/php/7.1/modules &&\  
cp /tmp/libs/nanocookiebulkuploader.ini /etc/php-7.1.d &&\  
rm -R /tmp/libs  

