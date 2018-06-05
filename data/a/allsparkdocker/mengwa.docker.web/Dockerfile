FROM allsparkdocker/mengwa.docker.web.base  
MAINTAINER "Neil Zeng" neil.zeng@gmail.com  
  
COPY ["config/ssh/neil.zeng@gmail.com", "config/ssh/ssh_config", "/etc/ssh/"]  
RUN cd /usr/src && \  
curl -o /usr/src/composer-setup.php https://getcomposer.org/installer && \  
curl -o /usr/src/composer-setup.sig https://composer.github.io/installer.sig
&& \  
php -r "if (hash('SHA384', file_get_contents('/usr/src/composer-setup.php'))
!== trim(file_get_contents('/usr/src/composer-setup.sig'))) {
unlink('/usr/src/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
ln -s /usr/src/composer.phar /usr/bin/composer && \  
mkdir -p ~/.ssh && \  
touch ~/.ssh/known_hosts && ssh-keyscan -t rsa gitee.com >> ~/.ssh/known_hosts
&& \  
chmod 400 /etc/ssh/neil.zeng@gmail.com && \  
cp -rp /etc/ssh/neil.zeng@gmail.com ~/.ssh/ && \  
cd /var && \  
git clone git@gitee.com:mengwa/common-auth.git common-auth && \  
git clone git@gitee.com:mengwa/common-db.git common-db && \  
git clone git@gitee.com:mengwa/mengwa.dc.back.ui.git app && \  
rm -rf /var/www && mv app www && \  
ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load && \  
usermod -u 1000 www-data && groupmod -g 1000 www-data && \  
chown www-data:www-data /etc/ssh/neil.zeng@gmail.com && \  
mkdir -p /var/www/.ssh && \  
cp -p ~/.ssh/known_hosts /var/www/.ssh && \  
chown -R www-data:www-data /var/www  
  
USER www-data  
RUN cd /var/www && composer install  
RUN cd /var/www && php artisan vendor:publish  
VOLUME /var/www/vendor  
VOLUME /var/www/.composer  
WORKDIR /var/www  
USER root  
RUN rm -rf /var/www/.ssh

