FROM xalauc/apache  
MAINTAINER Ben Blanks <ben@d15k.com>  
  
RUN echo PHPVERSION="7.1" >> /usr/local/bin/install_vars &&\  
echo XDEBUG="2.5.5" >> /usr/local/bin/install_vars &&\  
chmod a+x /usr/local/bin/install_vars  
##  
# Install the packages  
#  
RUN . /usr/local/bin/install_vars &&\  
apt-get update \--no-install-recommends -y &&\  
locale-gen en_US.UTF-8 &&\  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php \--yes &&\  
apt-get update \--no-install-recommends -y  
  
RUN . /usr/local/bin/install_vars &&\  
apt-get install \--no-install-recommends -y \  
php${PHPVERSION} \  
php${PHPVERSION}-cli \  
php${PHPVERSION}-curl \  
php${PHPVERSION}-dev \  
php${PHPVERSION}-gd \  
php${PHPVERSION}-ldap \  
php${PHPVERSION}-sqlite \  
php${PHPVERSION}-mysql \  
php${PHPVERSION}-opcache \  
php${PHPVERSION}-mcrypt \  
php${PHPVERSION}-mbstring \  
php${PHPVERSION}-mongodb \  
php${PHPVERSION}-json \  
php${PHPVERSION}-intl \  
php${PHPVERSION}-xml \  
php${PHPVERSION}-xsl \  
php${PHPVERSION}-zip  
  
##  
# Installing NPM so that we can install frontend build packages as part  
# of php project installs for frontend build processes.  
#  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN . /usr/local/bin/install_vars &&\  
apt-get install \--no-install-recommends -y nodejs &&\  
update-alternatives \--install /usr/bin/node node /usr/bin/nodejs 10  
  
##  
# Adding the PHP MOdule directory to the install vars file for later use.  
#  
RUN echo PHPMOD_DIR="$(php-config --extension-dir)" >>
/usr/local/bin/install_vars  
##  
# Clean the apt-get repo cache.  
#  
RUN . /usr/local/bin/install_vars &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
##############################################################################  
##  
##  
## Install the developer toolchain  
##  
##  
##############################################################################  
##  
# Installing PHP Unit  
#  
RUN . /usr/local/bin/install_vars &&\  
wget https://phar.phpunit.de/phpunit.phar &&\  
chmod a+x phpunit.phar &&\  
mv phpunit.phar /usr/local/bin/phpunit  
##  
# Installing wp-cli for use with wordpress projects.  
#  
RUN . /usr/local/bin/install_vars &&\  
wget https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
&&\  
chmod +x wp-cli.phar &&\  
mv wp-cli.phar /usr/local/bin/wp  
##  
# Installing composer.  
#  
RUN . /usr/local/bin/install_vars &&\  
curl -sS https://getcomposer.org/installer | php &&\  
mv composer.phar /usr/local/bin/composer  
##  
# Reconfigure PHP  
#  
RUN . /usr/local/bin/install_vars &&\  
sed -i 's/display_errors = Off/display_errors = On/g'
/etc/php/${PHPVERSION}/apache2/php.ini &&\  
sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 102M/g'
/etc/php/${PHPVERSION}/apache2/php.ini &&\  
sed -i 's/post_max_size = 8M/post_max_size = 108M/g'
/etc/php/${PHPVERSION}/apache2/php.ini &&\  
sed -i 's/;date.timezone =/date.timezone = "Australia\/Sydney"/g'
/etc/php/${PHPVERSION}/apache2/php.ini &&\  
sed -i 's/;error_log = syslog/error_log = syslog/g'
/etc/php/${PHPVERSION}/apache2/php.ini &&\  
phpenmod mcrypt &&\  
phpenmod ldap  
  
##  
# Install XDebug into PHP  
#  
RUN . /usr/local/bin/install_vars &&\  
wget http://xdebug.org/files/xdebug-${XDEBUG}.tgz &&\  
tar -xvzf xdebug-${XDEBUG}.tgz &&\  
rm xdebug-${XDEBUG}.tgz &&\  
cd xdebug-${XDEBUG} &&\  
phpize &&\  
./configure &&\  
make &&\  
mkdir -p ${PHPMOD_DIR} &&\  
cp modules/xdebug.so ${PHPMOD_DIR} &&\  
echo "[xdebug]" | tee -a /etc/php/${PHPVERSION}/apache2/conf.d/20-xdebug.ini >
/dev/null &&\  
echo "zend_extension = ${PHPMOD_DIR}/xdebug.so" | tee -a
/etc/php/${PHPVERSION}/apache2/conf.d/20-xdebug.ini > /dev/null &&\  
echo "xdebug.profiler_enable_trigger = 1" | tee -a
/etc/php/${PHPVERSION}/apache2/conf.d/20-xdebug.ini > /dev/null &&\  
echo "xdebug.profiler_output_dir = \"/var/www/profiler\"" | tee -a
/etc/php/${PHPVERSION}/apache2/conf.d/20-xdebug.ini > /dev/null &&\  
echo "[xdebug]" | tee -a /etc/php/${PHPVERSION}/cli/conf.d/20-xdebug.ini >
/dev/null &&\  
echo "zend_extension = ${PHPMOD_DIR}/xdebug.so" | tee -a
/etc/php/${PHPVERSION}/cli/conf.d/20-xdebug.ini > /dev/null &&\  
echo "xdebug.profiler_enable_trigger = 1" | tee -a
/etc/php/${PHPVERSION}/cli/conf.d/20-xdebug.ini > /dev/null &&\  
echo "xdebug.profiler_output_dir = \"/var/www/profiler\"" | tee -a
/etc/php/${PHPVERSION}/cli/conf.d/20-xdebug.ini > /dev/null &&\  
rm -rf /xdebug-${XDEBUG}

