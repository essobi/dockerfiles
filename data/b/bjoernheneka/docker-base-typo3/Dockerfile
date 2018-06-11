FROM ubuntu:trusty  
  
MAINTAINER Bjoern Heneka <bheneka@codebee.de>  
  
ENV TYPO3_VERSION 6.2.23  
ENV DB_HOST=db  
ENV DB_PORT=3306  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages required for TYPO3  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:nginx/stable && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y git \  
vim \  
supervisor \  
nginx \  
wget \  
mysql-client \  
php5-imagick \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-imagick \  
php5-mcrypt \  
php5-memcache \  
php5-mysql \  
php5-intl \  
graphicsmagick \  
locales \  
ccze && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean  
  
RUN sed -i 's/max_execution_time = .*/max_execution_time = '480'/'
/etc/php5/fpm/php.ini && \  
sed -i 's/upload_max_filesize = .*/upload_max_filesize = '100M'/'
/etc/php5/fpm/php.ini && \  
sed -i 's/post_max_size = .*/post_max_size = '100M'/' /etc/php5/fpm/php.ini &&
\  
echo "alias t3log='tail -f /var/log/apache2/*error*.log
typo3temp/logs/typo3.log | ccze -A'" >> /root/.bashrc && \  
mkdir -p /var/lib/typo3 && \  
cd /var/lib/typo3 && \  
wget -q -O -
http://prdownloads.sourceforge.net/typo3/typo3_src-${TYPO3_VERSION}.tar.gz |
tar zxf -  
  
RUN mkdir -p /var/www/site/htdocs && \  
cd /var/www/site/htdocs && \  
ln -s /var/lib/typo3/typo3_src-${TYPO3_VERSION} typo3_src && \  
ln -s typo3_src/index.php index.php && \  
ln -s typo3_src/typo3 typo3  
  
COPY docker/nginx.conf /etc/nginx/nginx.conf  
COPY docker/default.conf /etc/nginx/conf.d/default.conf  
COPY docker/start.sh /start.sh  
ADD docker/supervisord.conf /etc/supervisord.conf  
ADD docker/_.htaccess /tmp/_.htaccess  
  
RUN touch /FIRSTSTART  
  
RUN chmod 0755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]

