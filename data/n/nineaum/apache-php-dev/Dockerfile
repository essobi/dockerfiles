FROM ubuntu:trusty  
MAINTAINER 9AuM <aum@scriptdd.com>  
  
# Main Dockerfile ascdc/apache2-php56  
ADD run.sh /run.sh  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
chmod +x /*.sh && \  
apt-get update && \  
apt-get -y install software-properties-common python-software-properties && \  
locale-gen en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
add-apt-repository -y ppa:ondrej/php && \  
add-apt-repository -y ppa:ondrej/apache2  
  
RUN DEBIAN_FRONTEND=noninteractive && apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl nano apache2 php5.6 php5.6-common php5.6-json
php5.6-opcache php5.6-zip php5.6-mysql php5.6-phpdbg php5.6-gd php5.6-imap
php5.6-ldap php5.6-pgsql php5.6-pspell php5.6-recode php5.6-tidy php5.6-dev
php5.6-intl php5.6-curl php5.6-mcrypt php5.6-xmlrpc php5.6-xsl php5.6-bz2
php5.6-mbstring pkg-config libmagickwand-dev imagemagick build-essential
libapache2-mod-php5 && \  
echo 'autodetect'|pecl install imagick uploadprogress memcache && \  
echo "extension=imagick.so" | sudo tee /etc/php/5.6/mods-available/imagick.ini
&& \  
echo "extension=uploadprogress.so" | sudo tee /etc/php/5.6/mods-
available/uploadprogress.ini && \  
echo "extension=memcache.so" | sudo tee /etc/php/5.6/mods-
available/memcache.ini && \  
ln -sf /etc/php/5.6/mods-available/imagick.ini
/etc/php/5.6/apache2/conf.d/20-imagick.ini && \  
ln -sf /etc/php/5.6/mods-available/uploadprogress.ini
/etc/php/5.6/apache2/conf.d/20-uploadprogress.ini && \  
ln -sf /etc/php/5.6/mods-available/memcache.ini
/etc/php/5.6/apache2/conf.d/20-memcache.ini && \  
ln -sf ../mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load  
  
# ionCube  
RUN cd /tmp \  
&& apt-get install -y --no-install-recommends unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -xvvzf ioncube.tar.gz \  
&& mkdir /usr/lib/php5/ioncube \  
&& mv ioncube/ioncube_loader_lin_5.6.so /usr/lib/php5/ioncube/ioncube.so \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& bash -c "echo zend_extension = /usr/lib/php5/ioncube/ioncube.so >
/etc/php/5.6/apache2/conf.d/00-ioncube.ini" \  
&& bash -c "echo zend_extension = /usr/lib/php5/ioncube/ioncube.so >
/etc/php/5.6/cli/conf.d/00-ioncube.ini" \  
&& sed --in-place "s/^max_execution_time.*$/max_execution_time = 180/"
/etc/php/5.6/apache2/php.ini \  
&& sed --in-place "s/^post_max_size.*$/post_max_size = 500M/"
/etc/php/5.6/apache2/php.ini \  
&& sed --in-place "s/^upload_max_filesize.*$/upload_max_filesize = 500M/"
/etc/php/5.6/apache2/php.ini \  
&& sed --in-place "s/^memory_limit.*$/memory_limit = 500M/"
/etc/php/5.6/apache2/php.ini  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set ServerName  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Set Rewrite Config  
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride
None/AllowOverride all/' /etc/apache2/apache2.conf  
RUN a2enmod rewrite  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR /var/www/html  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

