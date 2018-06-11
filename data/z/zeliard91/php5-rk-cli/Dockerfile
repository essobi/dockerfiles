FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C && \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install curl git php7.1-fpm php7.1-gd php7.1-intl \  
php7.1-mcrypt php7.1-curl php7.1-mysql php7.1-sqlite php7.1-xml \  
php7.1-mbstring php7.1-zip php-memcached php-redis php7.1-zip php-ssh2 \  
wget xz-utils libqt4-network fontconfig libjpeg8 libxrender1 libxext6 xfonts-
base  
  
# Install wkhtmltox  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
apt-get -y install libssl-dev=1.0.2g-1ubuntu4.8 && \  
tar Jxvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
cp -r wkhtmltox/* /usr/local/ && \  
rm -rf wkhtmltox  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ADD www.conf /etc/php/7.1/fpm/pool.d/  
  
# create pid folder  
RUN mkdir /run/php  
  
CMD ["php-fpm7.1", "-F"]  
  
EXPOSE 9000  

