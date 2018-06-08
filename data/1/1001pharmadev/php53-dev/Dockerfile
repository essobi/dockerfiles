FROM debian:wheezy  
MAINTAINER Loïc Ambrosini <loic.ambrosini@me.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ADD docker/gitignore /root/.gitignore_global  
RUN echo "export TERM=xterm" >> /etc/bash.bashrc  
  
RUN echo deb http://snapshot.debian.org/archive/debian/20120221T041601Z/
unstable main >> /etc/apt/sources.list && \  
echo deb-src http://snapshot.debian.org/archive/debian/20120221T041601Z/
unstable main >> /etc/apt/sources.list  
  
# Install packages (multiple apt-get install due to debian http-redir error
not yet fixed)  
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get install -y \  
openssh-server \  
supervisor \  
git \  
make \  
curl \  
zsh \  
mysql-client \  
apache2.2-common  
RUN apt-get install -y \  
php5 \  
php5-dev \  
php5-curl \  
php5-imagick \  
php5-curl \  
php5-intl \  
php5-geoip  
RUN apt-get install -y \  
php-mime-type \  
php-pear \  
php5-mysql \  
php5-odbc \  
php5-xdebug \  
php5-xcache \  
php5-memcache  
  
# Supervisor config  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Php config (fix .so directories)  
RUN sed -i 's/memory_limit = .*/memory_limit = '512M'/'
/etc/php5/apache2/php.ini && \  
sed -i 's/memory_limit = .*/memory_limit = '512M'/' /etc/php5/cli/php.ini && \  
sed -i "s/^;date.timezone =$/date.timezone = \"Europe\/Paris\"/"
/etc/php5/cli/php.ini &&\  
sed -i "s/^;date.timezone =$/date.timezone = \"Europe\/Paris\"/"
/etc/php5/apache2/php.ini  
  
# Configure xDebug extension  
RUN sed -i '1 a xdebug.remote_autostart=true' /etc/php5/mods-
available/xdebug.ini && \  
sed -i '1 a xdebug.remote_connect_back=1 ' /etc/php5/mods-available/xdebug.ini
&& \  
sed -i '1 a xdebug.remote_enable=1' /etc/php5/mods-available/xdebug.ini && \  
sed -i '1 a xdebug.max_nesting_level=1200' /etc/php5/mods-available/xdebug.ini
&& \  
sed -i '1 a xdebug.idekey=PHPSTORM' /etc/php5/mods-available/xdebug.ini && \  
sed -i '1 a xdebug.collect_params=4' /etc/php5/mods-available/xdebug.ini && \  
sed -i '1 a xdebug.var_display_max_children=128' /etc/php5/mods-
available/xdebug.ini && \  
sed -i '1 a xdebug.var_display_max_data=1024' /etc/php5/mods-
available/xdebug.ini && \  
sed -i '1 a xdebug.var_display_max_depth=4' /etc/php5/mods-
available/xdebug.ini && \  
sed -i '1 a xdebug.show_local_vars=1' /etc/php5/mods-available/xdebug.ini  
  
# BlackFire  
RUN cd /tmp && mkdir blackfire && cd blackfire \  
&& curl -A "Docker" -o blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/54 \  
&& tar zxpf blackfire-probe.tar.gz \  
&& mv blackfire-*.so `php -r "echo ini_get('extension_dir');"`/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/etc/php5/cli/conf.d/blackfire.ini \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/etc/php5/apache2/conf.d/blackfire.ini \  
&& rm -Rf /tmp/*  
  
# Configure PHP  
RUN sed -i 's/= E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED/=
E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|E_CORE_ERROR/'
/etc/php5/apache2/php.ini && \  
sed -i 's/= E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED/=
E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|E_CORE_ERROR/'
/etc/php5/cli/php.ini  
  
# Configure default site (apache)  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ADD docker/vhost /etc/apache2/sites-available/000-default.conf  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
a2dissite default && \  
a2ensite 000-default.conf && \  
a2enmod rewrite ssl vhost_alias && \  
mkdir /var/www/html && \  
mkdir /var/www/html/web && \  
/etc/init.d/apache2 restart  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Node  
ADD docker/nodeInstall.sh /nodeInstall.sh  
RUN chmod +x ./nodeInstall.sh && \  
./nodeInstall.sh - && \  
apt-get install -y nodejs  
  
RUN npm install gulp-less && \  
npm install gulp-minify-css && \  
npm install gulp-uglify && \  
npm install gulp-concat  
  
# ZSH  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& chsh -s /bin/zsh && \  
echo "export TERM=xterm" >> ~/.zshrc && \  
sed -i -E "s/^plugins=\\((.*)\\)$/plugins=(\1 git common-aliases composer
phing symfony2)/" ~/.zshrc  
  
EXPOSE 22 80  
# Clean docker image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www/html  
  
ADD docker/start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD /start.sh  

