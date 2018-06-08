FROM overbid/7.0-apache  
  
LABEL maintainer="Eakkapat Pattarathamrong (overbid@gmail.com)"  
  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_2  
ENV ORACLE_HOME /opt/oracle/instantclient_12_2  
  
RUN set -x \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y \  
libaio-dev \  
libmcrypt-dev \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD instantclient_12_2.tar.gz /opt/oracle/  
RUN set -x \  
&& ln -s $LD_LIBRARY_PATH/libclntsh.so.12.1 $LD_LIBRARY_PATH/libclntsh.so \  
&& ln -s $LD_LIBRARY_PATH/libclntshcore.so.12.1
$LD_LIBRARY_PATH/libclntshcore.so \  
&& ln -s $LD_LIBRARY_PATH/libocci.so.12.1 $LD_LIBRARY_PATH/libocci.so \  
&& docker-php-ext-install \  
mcrypt \  
mysqli \  
zip \  
&& echo "instantclient,$ORACLE_HOME" | pecl install \  
oci8 \  
&& docker-php-ext-enable \  
oci8 \  
opcache  
  
RUN set -x \  
&& echo "Asia/Bangkok" | tee /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& echo '#' | tee /etc/apache2/ports.conf \  
&& echo 'date.timezone = "Asia/Bangkok"' | tee
/usr/local/etc/php/conf.d/locale.ini \  
&& echo 'default_charset = "utf-8"' | tee -a
/usr/local/etc/php/conf.d/locale.ini \  
&& echo "cgi.fix_pathinfo = 0" | tee -a /usr/local/etc/php/conf.d/file.ini \  
&& echo "upload_max_filesize = 8M" | tee -a /usr/local/etc/php/conf.d/file.ini
\  
&& a2enmod \  
expires \  
headers \  
http2 \  
include \  
proxy_fcgi \  
rewrite \  
setenvif \  
ssl \  
&& a2ensite \  
default-ssl \  
&& rm /etc/apache2/conf-enabled/charset.conf \  
&& rm /etc/apache2/conf-enabled/localized-error-pages.conf \  
&& rm /etc/apache2/conf-enabled/security.conf \  
&& rm /etc/apache2/mods-enabled/deflate.conf \  
&& sed -i "s/SSLCipherSuite/#SSLCipherSuite/g" /etc/apache2/mods-
available/ssl.conf \  
&& sed -i "s/SSLProtocol/#SSLProtocol/g" /etc/apache2/mods-available/ssl.conf  

