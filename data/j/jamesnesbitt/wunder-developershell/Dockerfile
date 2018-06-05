FROM jamesnesbitt/wunder-base  
MAINTAINER james.nesbitt@wunderkraut.com  
  
### DEVELOPER ---------------------------------------------------------------  
# Install some tools that are usefull for a developer  
RUN /usr/bin/yum --assumeyes --verbose install yum-utils openssl tar git zsh
sudo vim patch unzip p7zip which ansible  
  
# Allow passwordless sudo for the app user  
RUN /usr/bin/echo "app ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/app  
  
# Install nodejs and npm, which gets used for lots of stuff with SASS/SCSS  
RUN /usr/bin/yum install --assumeyes --verbose nodejs npm  
RUN /usr/bin/npm install gulp -g  
RUN /usr/bin/npm install grunt -g  
  
# Install the REMI repo : HOW NICE WOULD IT BE TO HAVE AN HTTPS ?!?  
RUN /usr/bin/yum install --assumeyes --verbose
http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
RUN yum-config-manager --enable remi-php70  
  
# Add some php extension configuraiton overrides  
ADD etc/php.d/01-defaultdatetime.ini /etc/php.d/01-defaultdatetime.ini  
ADD etc/php.d/40-apcu.ini /etc/php.d/40-apcu.ini  
  
# Install php-fpm - currently php7-rc5  
RUN /usr/bin/yum install --assumeyes --verbose \  
php-cli php-opcache php-pdo php-mysql php-pgsql \  
php-ldap php-gd php-mbstring php-mcrypt php-xml \  
php-pecl-apcu php-pecl-yaml php-pecl-uploadprogress php-pecl-zip  
  
# Install blackfire - still doesn't work as the blackfire install script
doesn't like our php7  
RUN curl "http://packages.blackfire.io/fedora/blackfire.repo" | tee
/etc/yum.repos.d/blackfire.repo  
RUN /usr/bin/yum install --assumeyes --verbose pygpgme php-cli blackfire-php  
RUN /usr/bin/yum remove --assumeyes --verbose php-cli  
ADD etc/php.d/zz-blackfire.ini /etc/php.d/zz-blackfire.ini  
  
# Install MariaDB  
ADD etc/yum.repos.d/mariadb.repo etc/yum.repos.d/mariadb.repo  
RUN /usr/bin/yum --assumeyes --verbose install MariaDB-client  
  
# Install composer which will be used to install drush  
RUN /usr/bin/yum install --assumeyes --verbose composer  
  
# Everything else is run as the platform user  
USER app  
  
# Add composer paths and app/bin to path  
ENV PATH
/app/bin:/app/.composer/vendor/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# Install Drupal console  
RUN /usr/bin/composer global require --optimize-autoloader --sort-packages
drupal/console  
  
# Install DRUSH,  
RUN /usr/bin/composer global require --optimize-autoloader --sort-packages
drush/drush pear/Console_Color2 drush/config-extra  
  
# Install platform.sh cli  
# RUN composer global require --optimize-autoloader --sort-packages
platformsh/cli # this conflicts with drupal console  
# RUN /usr/bin/composer global require --optimize-autoloader --sort-packages
platformsh/cli:@stable  
# Configure Platform CLI with this ENV var  
ENV PLATFORMSH_CLI_API_TOKEN %PLATFORMSH_CLI_API_TOKEN  
  
# Set up some folders for the tools that we just used  
RUN /usr/bin/mkdir /app/.platformsh && \  
/usr/bin/chown -R app:app /app/.platformsh && \  
/usr/bin/mkdir /app/.drush && \  
/usr/bin/chown -R app:app /app/.drush && \  
/usr/bin/mkdir /app/.ssh && \  
/usr/bin/chown -R app:app /app/.ssh  
  
# Some usefull env variables  
ENV TERM=xterm  
  
#CMD ["/bin/bash"]  
### /DEVELOPER ---------------------------------------------------------------  
### James Developer ----------------------------------------------------------  
USER app  
  
# Make the app user use the zsh shell with oh-my-zsh installed  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
ADD .zshrc /app/.zshrc  
  
USER root  
  
# Change the default shell to zsh, and add a nice zsh prompt  
RUN /usr/sbin/usermod -s /bin/zsh app && \  
chown -R app:app /app/.zshrc /app/.oh-my-zsh  
  
USER app  
CMD ["/usr/bin/ssh-agent","/bin/zsh"]  
  
### /James Developer ---------------------------------------------------------  

