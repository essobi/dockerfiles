FROM uofa/apache2-php7:shepherd  
  
# Add the chromedriver repo using php, no wget or curl yet.  
RUN php -n -r 'echo file_get_contents("https://dl-
ssl.google.com/linux/linux_signing_key.pub");' | apt-key add - \  
&& echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main'
> /etc/apt/sources.list.d/google-chrome.list  
  
# Upgrade all currently installed packages and install web server packages.  
RUN apt-get update \  
&& apt-get -y install php-sqlite3 php-xdebug php7.2-cli git wget sudo unzip
libnotify-bin google-chrome-stable \  
&& sed -ri 's/^zend.assertions\s*=\s*-1/zend.assertions = 1/g'
/etc/php/7.2/cli/php.ini \  
&& sed -i 's/^\\(allow_url_fopen\s*=\s*\\).*$/\1on/g' /etc/php/7.2/mods-
available/php_custom.ini \  
&& CHROME_DRIVER_VERSION=$(php -n -r 'echo
file_get_contents("https://chromedriver.storage.googleapis.com/LATEST_RELEASE");')
\  
&& wget
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& unzip chromedriver_linux64.zip -d /usr/local/bin \  
&& rm chromedriver_linux64.zip \  
&& chmod +x /usr/local/bin/chromedriver \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get clean && rm -rf
/var/lib/apt/lists /tmp/* /var/tmp/*  
  
# Install Composer.  
RUN wget -q https://getcomposer.org/installer -O - | php -d allow_url_fopen=On
-- --install-dir=/usr/local/bin --filename=composer  
  
# Configure additional PHP modules.  
COPY ./files/xdebug.ini /etc/php/7.2/mods-available/xdebug.ini  
  
# Enable xdebug.  
RUN phpenmod -v ALL -s ALL xdebug  

