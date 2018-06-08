FROM trovit/php-simulation:56  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
git \  
vim \  
wget \  
openssh-server \  
php5-xdebug \  
unzip \  
daemon \  
telnet \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY conf/xdebug.ini /etc/php5/mods-available/xdebug.ini  
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN ln -s /etc/php5/mods-available/xdebug.ini
/etc/php5/cli/conf.d/20-xdebug.ini  
  
# Install composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
# Make sure we're installing what we think we're installing!  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
  
# SSHD daemon setup as per the official documentation  
# at https://docs.docker.com/engine/examples/running_ssh_service/  
RUN mkdir /var/run/sshd \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# FPM child processes run as root  
RUN sed -i 's@user = www-data@user = root@' /etc/php5/fpm/pool.d/www.conf \  
&& sed -i 's@group = www-data@group = root@' /etc/php5/fpm/pool.d/www.conf  
  
EXPOSE 22 9000  
ENV TINI_VERSION v0.13.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
ENTRYPOINT ["/tini", "--"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

