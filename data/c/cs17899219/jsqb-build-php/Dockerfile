FROM ubuntu:14.04  
MAINTAINER Joseph zhou "joseph.zhou@gmail.com"  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# TimeZone  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# Update source  
### RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g'
/etc/apt/sources.list  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update --fix-missing && apt-get upgrade -y -q && \  
apt-get install -y unzip git rsync curl tree vim openssl language-pack-en-base
software-properties-common && \  
apt-get clean  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php -y  
RUN apt-get update --fix-missing && apt-get -y install php7.0-dev php7.0-fpm
php7.0-gd php7.0-xml php7.0-mysql \  
php7.0-mcrypt php7.0-curl php7.0-mbstring php7.0-imagick php7.0-mongodb
php7.0-redis && \  
apt-get clean  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
chmod +x /usr/local/bin/composer  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

