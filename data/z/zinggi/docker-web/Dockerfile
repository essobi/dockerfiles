FROM php:7.1-apache  
MAINTAINER Christian Zingg <mich-web@zinggi.ch>  
  
  
# Setup  
ENV WWW_DIR /var/www  
ENV ROOT_DIR ${WWW_DIR}/html  
  
ENV TOOLS_DIR ${ROOT_DIR}/.tools  
  
ENV TYPO3_VERSION_BRANCH 8  
ENV COMPOSER_DIR ${WWW_DIR}/.composer  
ENV COMPOSER_VERSION 1.6.2  
# Add tools  
RUN mkdir ${TOOLS_DIR}  
ADD ./tools ${TOOLS_DIR}  
VOLUME $TOOLS_DIR  
  
# Install Libraries  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
wget \  
mysql-client \  
graphicsmagick \  
imagemagick \  
libxml2-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
git \  
rsync  
  
# Install TYPO3  
RUN cd ${ROOT_DIR} && \  
wget -O - https://get.typo3.org/${TYPO3_VERSION_BRANCH} | tar -xzf - && \  
ln -s typo3_src-* typo3_src && \  
ln -s typo3_src/index.php && \  
ln -s typo3_src/typo3 && \  
cp typo3_src/_.htaccess .htaccess && \  
touch FIRST_INSTALL  
  
# Configure Apache  
RUN a2enmod rewrite  
  
# Configure PHP  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mcrypt mysqli opcache pdo pdo_mysql soap gd
zip  
RUN echo 'date.timezone = Europe/Zurich\ndisplay_errors =
On\ndisplay_startup_errors = On\nlog_errors = Off\nerror_reporting = E_ALL' >
/usr/local/etc/php/conf.d/settings.ini  
RUN echo 'always_populate_raw_post_data = -1\nmax_execution_time =
240\nmax_input_vars = 1500\nupload_max_filesize = 32M\npost_max_size = 32M' >
/usr/local/etc/php/conf.d/typo3.ini  
  
# Install SSMTP  
RUN apt-get install --no-install-recommends -y \  
ssmtp && \  
groupadd -g 500 ssmtp && \  
chown :ssmtp /usr/sbin/ssmtp && \  
chmod g+s /usr/sbin/ssmtp && \  
echo "sendmail_path = /usr/sbin/ssmtp -t" >
/usr/local/etc/php/conf.d/sendmail.ini  
ADD ./conf/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
# Install composer  
ENV PATH vendor/bin:$COMPOSER_DIR/vendor/bin:$PATH  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
\--version=${COMPOSER_VERSION}  
RUN mkdir -p $COMPOSER_DIR/cache && \  
echo "phar.readonly = off" > /usr/local/etc/php/conf.d/phar.ini  
VOLUME $COMPOSER_DIR/cache  
  
# Change ownership  
RUN chown -R www-data:www-data ${WWW_DIR}  

