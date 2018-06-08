# This is a Dockerfile for build a opensuse image wihch include apache2 and
php5  
FROM mengzyou/docker-opensuse-base:latest  
MAINTAINER Mengz You <mengz.you@outlook.com>  
  
# ENV  
ENV APACHE_VERSION 2.4.16  
ENV PHP_VERSION 5.6.9  
# Add server_php repository  
RUN zypper -q ar -f -r
http://download.opensuse.org/repositories/server:/php/openSUSE_13.2/server:php.repo
\  
&& zypper -q ar -f -r
http://download.opensuse.org/repositories/Apache/openSUSE_13.2/Apache.repo  
  
# Refresh repositories and install packages  
RUN zypper -qn --gpg-auto-import-keys ref \  
&& zypper -qn in -l --no-recommends apache2-$APACHE_VERSION
apache2-mod_php5-$PHP_VERSION php5-$PHP_VERSION php5-ctype-$PHP_VERSION
php5-dom-$PHP_VERSION php5-iconv-$PHP_VERSION php5-json-$PHP_VERSION
php5-sqlite-$PHP_VERSION php5-tokenizer-$PHP_VERSION
php5-xmlreader-$PHP_VERSION php5-xmlwriter-$PHP_VERSION php5-gd-$PHP_VERSION
php5-gettext-$PHP_VERSION php5-mbstring-$PHP_VERSION php5-mysql-$PHP_VERSION
php5-pear-$PHP_VERSION php5-suhosin-$PHP_VERSION \  
&& zypper clean -a  
  
# Open apache rewrite and php5 module and disable userdir module  
RUN a2enmod rewrite \  
&& a2enmod php5 \  
&& a2dismod userdir  
  
# Set Volume  
VOLUME ["/srv/www/htdocs"]  
  
# Add a test file  
ADD files/index.php /srv/www/htdocs/index.php  
  
# Entrypoint  
ENTRYPOINT ["start_apache2"]  
  
# Expose ports  
EXPOSE 80  
# Start apache  
CMD ["-DFOREGROUND"]  

