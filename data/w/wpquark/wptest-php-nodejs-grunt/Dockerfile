# Dockerfile for generating a WordPress friendly container  
# Run unittests, build with grunt or install your own packages with npm  
# Start from php image  
FROM php:7.0  
# Maintainer  
MAINTAINER Swashata Ghosh <swashata4u@gmail.com>  
  
# Non interactive mode  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Update our repository  
RUN apt-get update -yqq  
  
# Install git  
RUN apt-get install git -yqq  
  
# Install core dependencies  
RUN apt-get install -yqqf --fix-missing \  
vim wget curl zip unzip subversion mysql-client libmcrypt-dev libmysqlclient-
dev openssh-client gettext libfreetype6-dev libjpeg62-turbo-dev libpng12-dev
xvfb fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-
cyrillic python  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# Install Google Chrome  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get -yqq update && \  
apt-get -yqq install google-chrome-stable && \  
rm -rf /var/lib/apt/lists/*  
  
# Default configuration  
ENV DISPLAY :20.0  
ENV SCREEN_GEOMETRY "1440x900x24"  
ENV CHROMEDRIVER_PORT 4444  
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"  
ENV CHROMEDRIVER_URL_BASE ''  
# Install PHP Extensions  
RUN docker-php-ext-install mysqli pdo_mysql mbstring mcrypt zip  
  
# Configure PHP-GD  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
# Install XDEBUG  
RUN pecl install xdebug  
  
# Enable needed PHP extensions  
RUN docker-php-ext-enable mysqli pdo_mysql mbstring xdebug mcrypt zip gd  
  
# Install PHPUnit tests  
RUN wget https://phar.phpunit.de/phpunit-6.3.phar && \  
chmod +x phpunit-6.3.phar && \  
mv phpunit-6.3.phar /usr/local/bin/phpunit  
  
# Install composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer && rm -rf /tmp/composer-setup.php  
  
# Install WP-CLI  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
  
# Install Node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install -yqq nodejs  
  
# Install grunt-cli  
RUN npm install -g grunt-cli  
  
# Install bower  
RUN npm install -g bower  
  
# Setup WordPress PHPUnit Testing environment  
# Setup environment  
ENV WP_CORE_DIR "/tmp/wordpress/"  
ENV WP_TESTS_DIR "/tmp/wordpress-tests-lib"  
ENV WP_VERSION "4.8.1"  
ENV WP_TESTS_TAG "tags/4.8.1"  
# Download WordPress from source  
RUN mkdir -p $WP_CORE_DIR  
RUN curl -s "https://wordpress.org/wordpress-${WP_VERSION}.tar.gz" >
"/tmp/wordpress.tar.gz" && \  
tar --strip-components=1 -zxmf /tmp/wordpress.tar.gz -C $WP_CORE_DIR  
  
# Get the test data from SVN  
RUN mkdir -p $WP_TESTS_DIR && \  
svn co --quiet
https://develop.svn.wordpress.org/${WP_TESTS_TAG}/tests/phpunit/includes/
$WP_TESTS_DIR/includes && \  
svn co --quiet
https://develop.svn.wordpress.org/${WP_TESTS_TAG}/tests/phpunit/data/
$WP_TESTS_DIR/data  
  
# Setup initial SSH agent  
RUN mkdir -p ~/.ssh && \  
eval $(ssh-agent -s) && \  
echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  
  
# Setup Sonar Scanner  
RUN cd ~  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.0.3.778-linux.zip  
RUN unzip sonar-scanner-cli-3.0.3.778-linux.zip  
RUN mv sonar-scanner-3.0.3.778-linux /opt/sonar-scanner/  
RUN rm -f sonar-scanner-cli-3.0.3.778-linux.zip  
ENV PATH="/opt/sonar-scanner/bin:${PATH}"  
RUN sonar-scanner -h  
  
# Install gulp  
RUN npm install -g gulp-cli  
  
## That's it, let pray it works  

