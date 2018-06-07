FROM ubuntu:16.04  
RUN apt update  
RUN export LANG=C.UTF-8  
RUN apt install -y software-properties-common  
RUN export LANG=C.UTF-8 && add-apt-repository -y ppa:ondrej/php  
RUN apt update  
RUN apt install -y \  
git \  
curl \  
wget \  
zsh \  
nano \  
supervisor \  
nginx \  
php5.6 \  
php5.6-fpm \  
php5.6-cli \  
php5.6-curl \  
php5.6-zip \  
php5.6-json \  
php5.6-mysql \  
php5.6-pgsql \  
php5.6-mcrypt \  
php5.6-mbstring \  
php5.6-gd \  
php5.6-xml \  
php5.6-xdebug  
  
RUN apt autoremove -y && \  
apt clean && \  
apt autoclean  
  
RUN mkdir /run/php/  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i "s/display_errors = On/display_errors = Off/"
/etc/php/5.6/fpm/php.ini  
RUN sed -i "s/user = www-data/user = root/" /etc/php/5.6/fpm/pool.d/www.conf  
RUN sed -i "s/group = www-data/group = root/" /etc/php/5.6/fpm/pool.d/www.conf  
  
# Supervisor conf  
RUN echo "[supervisord]" >> /etc/supervisor/supervisord.conf  
RUN echo "nodaemon = true" >> /etc/supervisor/supervisord.conf  
RUN echo "user = root" >> /etc/supervisor/supervisord.conf  
  
RUN echo "[program:php-fpm5.6]" >> /etc/supervisor/supervisord.conf  
RUN echo "command = /usr/sbin/php-fpm5.6 -FR" >>
/etc/supervisor/supervisord.conf  
RUN echo "autostart = true" >> /etc/supervisor/supervisord.conf  
RUN echo "autorestart = true" >> /etc/supervisor/supervisord.conf  
  
RUN echo "[program:nginx]" >> /etc/supervisor/supervisord.conf  
RUN echo "command = /usr/sbin/nginx" >> /etc/supervisor/supervisord.conf  
RUN echo "autostart = true" >> /etc/supervisor/supervisord.conf  
RUN echo "autorestart = true" >> /etc/supervisor/supervisord.conf  
  
#Xdebug  
#RUN echo "zend_extension=xdebug.so" >> /etc/php/5.6/mods-available/xdebug.ini  
RUN echo "xdebug.remote_enable = 1" >> /etc/php/5.6/mods-available/xdebug.ini  
RUN echo "xdebug.remote_port = 9000" >> /etc/php/5.6/mods-available/xdebug.ini  
RUN echo "xdebug.idekey = PHPSTORM" >> /etc/php/5.6/mods-available/xdebug.ini  
RUN echo "xdebug.show_error_trace = 1" >> /etc/php/5.6/mods-
available/xdebug.ini  
RUN echo "xdebug.remote_autostart = 0" >> /etc/php/5.6/mods-
available/xdebug.ini  
RUN echo "xdebug.file_link_format = phpstorm://open?%f:%l" >>
/etc/php/5.6/mods-available/xdebug.ini  
  
# Install Zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && cp
~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
RUN sed -i "s/robbyrussell/af-magic/" ~/.zshrc  
RUN echo TERM=xterm >> /root/.zshrc  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
CMD ["/usr/bin/supervisord"]  

