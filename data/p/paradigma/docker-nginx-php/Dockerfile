FROM million12/nginx:latest  
MAINTAINER Greco Rubio <greco@paradigma.com.mx>  
  
RUN \  
rpm --rebuilddb && yum update -y && \  
`# Install yum-utils (provides yum-config-manager) + some basic web-related
tools...` \  
yum install -y yum-utils wget patch tar bzip2 unzip openssh-clients rsync && \  
  
`# Install PHP 5.6` \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \  
yum-config-manager -q --enable remi && \  
yum-config-manager -q --enable remi-php56 && \  
yum install -y php-fpm php-bcmath php-cli php-gd php-intl php-mbstring \  
php-pecl-imagick php-mcrypt php-mysqlnd php-opcache php-pdo \  
php-xml php-zip php-iconv php-curl php-simplexml php-dom \  
php-pecl-apc php-pear php-pgsql php-pecl-mongo php-pecl-memcache php-pecl-
memcached && \  
yum install -y --disablerepo=epel php-pecl-redis php-pecl-yaml && \  
  
`# Install libs required to build some gem/npm packages (e.g. PhantomJS
requires zlib-devel, libpng-devel)` \  
yum install -y ImageMagick GraphicsMagick gcc gcc-c++ libffi-devel libpng-
devel zlib-devel && \  
  
`# Install common tools needed/useful during Web App development` \  
  
yum clean all && rm -rf /tmp/yum* && \  
  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chown www /usr/local/bin/composer  
  
ADD container-files /  
  
ENV STATUS_PAGE_ALLOWED_IP=127.0.0.1  

