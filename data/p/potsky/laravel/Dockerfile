############################################################  
# Dockerfile to build container with :  
# - Apache 2.4  
# - PHP 7.0  
# - xDebug  
# - mySQL  
# - Redis  
# Based on Debian  
############################################################  
# Build a Debian  
FROM debian:jessie  
MAINTAINER potsky <potsky@me.com>  
  
# Non interactive mode for mysql install for example  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install basics  
RUN apt-get update && apt-get install -y \  
apt-utils \  
curl \  
wget  
  
# Add dotdeb  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list  
RUN wget https://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg && rm
dotdeb.gpg  
  
# Add nodesource  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
# Update the repository sources list  
# Install basics again  
# Install MySQL  
# Install Redis  
# Install Superisor  
# Install SSH Server  
# Install Apache  
# Install PHP  
RUN apt-get update && apt-get install -y \  
zsh \  
git \  
vim \  
htop \  
vim \  
htop \  
mysql-server \  
redis-server \  
supervisor \  
openssh-server \  
apache2 \  
apache2-bin \  
apache2-data \  
apache2-utils \  
php7.0 \  
php7.0-apcu \  
php7.0-mysql \  
php7.0-redis \  
php7.0-mbstring \  
php7.0-opcache \  
php7.0-xml \  
php7.0-xdebug \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-zip \  
php7.0-bz2 \  
telnet \  
unzip \  
nodejs  
  
# Run oh my zsh  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
-O - | zsh || true  
  
# Configure System  
ADD config/system/rc.local /etc/rc.local  
ADD config/system/motd /etc/motd  
  
# Configure Supervisord  
ADD config/supervisor/app.conf /etc/supervisor/conf.d/app.conf  
  
# Configure SSH Server  
RUN sed -ie 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
# Set root password  
RUN echo "root:root" | chpasswd  
RUN chsh -s /bin/zsh root  
  
# Configure Timezone  
RUN echo "" >> /etc/profile  
RUN echo "TZ='Europe/Paris'; export TZ" >> /etc/profile  
  
RUN echo "" >> /etc/zsh/zshrc  
RUN echo "TZ='Europe/Paris'; export TZ" >> /etc/zsh/zshrc  
RUN echo "" >> /etc/zsh/zshrc  
RUN echo "myip() { ip addr show | grep inet | grep eth0 | awk '{print \$2}' |
cut -d'/' -f1 }" >> /etc/zsh/zshrc  
RUN echo "" >> /etc/zsh/zshrc  
RUN echo 'alias aa="tail -100f /var/log/apache2/access.log"' >> /etc/zsh/zshrc  
RUN echo 'alias ae="tail -100f /var/log/apache2/error.log"' >> /etc/zsh/zshrc  
RUN echo 'alias phpunit="vendor/bin/phpunit"' >> /etc/zsh/zshrc  
RUN echo 'alias art="php artisan"' >> /etc/zsh/zshrc  
RUN echo 'alias xdebug="export XDEBUG_CONFIG=\"idekey=PHPSTORM\""' >>
/etc/zsh/zshrc  
  
# Configure MySQL  
ADD config/mysql/debian.cfg /etc/mysql/debian.cfg  
  
# Configure Apache  
RUN a2enmod rewrite  
ADD config/apache/app.conf /etc/apache2/sites-enabled/000-default.conf  
RUN rm /var/www/html/index.html  
ADD files/app_tools /var/www/html  
  
# Configure PHP  
ADD config/php/xdebug.ini /etc/php/7.0/apache2/conf.d/20-xdebug.ini  
RUN sed -ie 's/memory_limit\ =\ 128M/memory_limit\ =\ 2G/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ie 's/\;date\\.timezone\ =/date\\.timezone\ =\ Europe\/Paris/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ie 's/upload_max_filesize\ =\ 2M/upload_max_filesize\ =\ 200M/g'
/etc/php/7.0/apache2/php.ini  
RUN sed -ie 's/post_max_size\ =\ 8M/post_max_size\ =\ 200M/g'
/etc/php/7.0/apache2/php.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Git Global  
ADD files/gitignore-global /root/.gitignore-global  
RUN git config --global core.excludesfile ~/.gitignore-global  
RUN git config --global --add oh-my-zsh.hide-dirty 1  
  
# Ngrok  
ADD files/ngrok /usr/local/bin/ngrok  
RUN chmod +x /usr/local/bin/ngrok  
  
# Install PHPMyAdmin  
RUN cd /var/www/html; git clone \--depth=1
https://github.com/phpmyadmin/phpmyadmin.git;  
RUN cd /var/www/html/phpmyadmin; composer install  
ADD config/phpmyadmin/config.inc.php /var/www/html/phpmyadmin/config.inc.php  
  
# Install PimpMyLogs  
RUN cd /var/www/html; git clone https://github.com/potsky/PimpMyLog.git  
ADD config/pimpmylog/config.user.json /var/www/html/PimpMyLog/config.user.json  
  
# Install PHPRedMin  
RUN cd /var/www/html; git clone https://github.com/sasanrose/phpredmin.git  
ADD config/phpredmin/config.php /var/www/html/phpredmin/config.php  
  
# Install MailDev  
RUN npm install -g maildev  
  
# Envoy  
RUN composer global require "laravel/envoy=~1.0"  
RUN echo "" >> /root/.zshrc  
RUN echo "export
PATH=\$HOME/.composer/vendor/bin:\$HOME/bin:/usr/local/bin:\$PATH" >>
/root/.zshrc  
  
# Set correct rights  
RUN chown -R www-data:www-data /var/www/html  
  
# Set root password  
RUN echo "root:root" | chpasswd  
RUN chsh -s /bin/zsh root  
  
# Open ports  
EXPOSE 22  
EXPOSE 80  
# Link Laravel App  
RUN mkdir /app  
WORKDIR /app  
  
# Configure persistent Volumes  
VOLUME ["/var/lib/mysql"]  
  
# Run  
RUN mkdir -p /root/script /root/config  
ADD files/run.sh /root/script/run.sh  
RUN chmod +x /root/script/run.sh  
  
CMD [ "/root/script/run.sh" ]  

