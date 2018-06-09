FROM centos:6.7  
MAINTAINER takara  
  
WORKDIR /root  
  
RUN yum -y update && \  
yum -y install ntp nginx vim git sysstat imagemagick imagemagick-devel ntpd
telnet mailx wget zip sharutil sudo  
  
RUN wget http://ftp-
srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm ; \  
yum -y install epel-release-6-8.noarch.rpm ; \  
rm epel-release-6-8.noarch.rpm ; \  
wget wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm ; \  
yum -y install remi-release-6.rpm ; \  
rm remi-release-6.rpm ; \  
exit 0  
  
RUN yum -y install mysql mysql-server nginx  
  
RUN chkconfig postfix off  
  
RUN yum -y install --enablerepo=epel libtidy libmcrypt && \  
yum -y install --enablerepo=remi-php56,remi \  
php \  
php-cli \  
php-common \  
php-devel \  
php-mbstring \  
php-mysql \  
php-pdo \  
php-pear \  
php-xml \  
php-pecl-redis \  
php-pecl-ssh2 \  
php-tidy \  
php-pecl-imagick \  
php-opcache \  
php-bcmath \  
php-mcrypt \  
php-fpm  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv /root/composer.phar /usr/bin/composer && \  
chmod +x /usr/bin/composer  
  
RUN composer global require hirak/prestissimo  
  
RUN echo "export PATH=\${PATH}:/var/www/vendor/bin:." >> .bashrc  
RUN chkconfig iptables off  
RUN chkconfig nginx on  
RUN chkconfig php-fpm on  
  
COPY asset/etc/* /etc/  
COPY asset/etc/nginx/conf.d/default.conf /etc/nginx/conf.d/  
COPY asset/etc/php-fpm.d/www.conf /etc/php-fpm.d/  
COPY asset/root/.vimrc /root/  
  
RUN sed -i "s/^\\(\/sbin\/start_udev\\)$/#\1/" /etc/rc.d/rc.sysinit  
RUN sed -i "s/^\\(exec\\)/#\1/" /etc/init/tty.conf  
  
WORKDIR /var/www  

