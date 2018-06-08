#  
# THIS IMAGE IS FOR DEVELOPMENT ONLY!  
#  
FROM mihailbinev/php7-fpm  
MAINTAINER Mihail Binev <mihail@kodeart.com>  
  
# install dev tools, libs  
RUN apt-get update && apt-get install -y git curl dnsutils openssh-server
libbz2-dev && \  
docker-php-ext-install bz2 && \  
mkdir -p /var/run/sshd  
  
# composer, phpunit, phpmd, phpcs, xdebug  
RUN curl -jksSL https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin && \  
chmod +x /usr/local/bin/composer && \  
curl -jksSL http://static.phpmd.org/php/latest/phpmd.phar -o
/usr/local/bin/phpmd && \  
curl -jksSL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o
/usr/local/bin/phpcs && \  
curl -jksSL https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit &&
\  
chmod +x /usr/local/bin/phpunit /usr/local/bin/phpcs /usr/local/bin/phpmd && \  
pecl install xdebug && \  
docker-php-ext-enable xdebug  
  
# cleanup  
RUN apt-get -y autoremove && apt-get autoclean && apt-get clean && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# add supervisor sshd program  
ADD config-files /  
  
# sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

