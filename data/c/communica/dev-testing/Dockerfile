FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN apt-get install -y \  
curl \  
build-essential \  
mariadb-server \  
git \  
python \  
python-pip \  
ruby \  
ruby-dev \  
bundler \  
php \  
php-cli \  
php-xml \  
php-curl \  
php-mbstring  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs  
  
# Slim down image  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/??
/usr/share/man/??_*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin  
RUN composer global require hirak/prestissimo  
RUN export PATH="$PATH:$HOME/.composer/vendor/bin"  
  
# Install packages  
RUN composer global require squizlabs/php_codesniffer:2.9  
RUN composer global require drupal/coder  
RUN ln -s /root/.composer/vendor/bin/phpcs /usr/bin/phpcs  
RUN ln -s /root/.composer/vendor/bin/phpcbf /usr/bin/phpcbf  
RUN phpcs --config-set installed_paths
/root/.composer/vendor/drupal/coder/coder_sniffer  
RUN phpcbf --config-set installed_paths
/root/.composer/vendor/drupal/coder/coder_sniffer  
RUN composer global require phpmd/phpmd  
RUN gem install scss_lint  
RUN npm install -g cypress  
RUN composer global require drupal/console --optimize-autoloader  
RUN ln -s /root/.composer/vendor/bin/drupal /usr/bin/drupal  
RUN composer global require drush/drush  
RUN ln -s /root/.composer/vendor/bin/drush /usr/bin/drush  
  
# Install terminus  
RUN composer global require pantheon-systems/terminus  
RUN ln -s /root/.composer/vendor/bin/terminus /usr/bin/terminus  
  
# Get Lint config  
RUN git clone https://bitbucket.org/garethhallnz/scss-lint-config.git  
RUN cd /scss-lint-config/ && git pull  
RUN mv /scss-lint-config/.scss-lint.yml ~/  
  
# Install pip and aws tools  
RUN pip install awscli  
  
# Start mysql  
RUN /etc/init.d/mysql start  
  
# Show versions  
RUN php -v  
RUN node -v  
RUN npm -v  
RUN cypress -v  
RUN ruby -v  
RUN bundle -v  
RUN phpcs -i  
RUN scss-lint -v  
RUN terminus --version  
RUN drush --version  
RUN which drupal  

