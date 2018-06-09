FROM centos:7  
MAINTAINER "Egor Zyuskin" <e.zyuskin@tree-soft.com>  
  
ADD ./etc/yum.repos.d/ /etc/yum.repos.d/  
ADD ./usr/ /usr/  
  
RUN rpm -i http://mirror.yandex.ru/epel/7Server/x86_64/e/epel-
release-7-9.noarch.rpm && \  
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \  
ln -s /usr/sbin/composer.phar /usr/sbin/composer && \  
ln -s /usr/sbin/phpunit.phar /usr/sbin/phpunit  
  
RUN yum install -y php56w php56w-gd php56w-intl php56w-mbstring php56w-xml
php56w-mcrypt php56w-pecl-apcu php56w-opcache php56w-soap php56w-tidy
php56w-pgsql php56w-mysql php56w-fpm nodejs supervisor nginx git sudo cronie-
noanacron unzip which  
  
RUN composer global require fxp/composer-asset-plugin:1.2.2  
  
RUN yum clean all && \  
rm -f -R /var/www/html /var/www/cgi-bin  
  
ADD ./etc/ /etc/  
  
WORKDIR /var/www  
  
VOLUME ["/var/www/", "/var/log/", "/root/.composer", "/etc/nginx/ssl"]  

