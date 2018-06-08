# Spoke Dockerfile for owncloud  
  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
curl libcurl3 bzip2 wget openssl ssl-cert sharutils libmcrypt4 \  
ffmpegthumbnailer smbclient php5 php5-fpm php5-gd php-xml-parser php5-intl \  
php5-pgsql php5-curl liboauth-php libphp-pclzip libphp-phpmailer php-file \  
php-aws-sdk php-crypt-blowfish php-doctrine-common php-dompdf php-dropbox \  
php-font-lib php-getid3 php-google-api-php-client php-guzzle php-irods-prods \  
php-opencloud php-patchwork-utf8 php-pear php-phpdocx php-sabre-dav \  
php-sabre-vobject php-seclib php-services-json php-symfony-console \  
php-symfony-eventdispatcher php-symfony-routing php-fpdf php5-apcu php5-cli \  
php5-common php5-imagick php-net-ftp php5-gmp php5-json php5-ldap php5-mcrypt
\  
php5-oauth php5-readline php5-tidy php5-xsl sdop zend-framework \  
zend-framework-bin libzend-framework-php &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
# Process startup info  
ENV SPOKE_NAME ocApp  
  
COPY /entrypoint.sh /entrypoint.sh  

