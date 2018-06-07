FROM php:7.0.7-fpm  
  
### Install Others  
RUN apt-get update && apt-get install -y git wget zlib1g-dev libmcrypt-dev
supervisor openssh-server \  
&& mkdir -p /var/log/supervisor \  
&& mkdir -p /var/run/sshd \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install bcmath mbstring opcache pcntl zip mcrypt pdo_mysql
opcache  
## Xdebug  
RUN pecl install xdebug-beta \  
&& docker-php-ext-enable xdebug  
  
# Install APCu  
RUN pecl install apcu-5.1.3 \  
&& docker-php-ext-enable apcu  
  
#Add composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
COPY supervisor/supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY php.ini /usr/local/etc/php/php.ini  
COPY php-fpm.conf /usr/local/etc/php-fpm.conf  
  
RUN useradd -ms /bin/bash jarco  
RUN usermod -u 1000 jarco  
  
# SSH config  
RUN echo 'root:jarcodev' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& sed -i 's@user = nobody@user = root@' /usr/local/etc/php-fpm.conf \  
&& sed -i 's@group = nobody@group = root@' /usr/local/etc/php-fpm.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
  
WORKDIR /app  

