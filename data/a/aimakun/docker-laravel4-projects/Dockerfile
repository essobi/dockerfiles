FROM parana/trusty-php  
  
COPY docker-vhosts.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Set timezone  
RUN echo 'date.timezone = Asia/Bangkok' > /etc/php5/apache2/php.ini  
  
# Required extensions for this project  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
software-properties-common wget php5-mcrypt php-soap php5-intl \  
libcurl3 php5-curl gettext \  
xvfb libxrender1 \  
&& php5enmod mcrypt \  
&& php5enmod soap \  
&& a2enmod headers  
  
# Install wkhtmltopdf  
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \  
&& cp wkhtmltox/bin/wkhtmltopdf /usr/bin \  
&& cp wkhtmltox/bin/wkhtmltoimage /usr/bin \  
&& rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \  
&& rm -r wkhtmltox  
  
# Install PHP CodeSniffer  
RUN pear install PHP_CodeSniffer  
  
# Setup locale & timezone  
RUN locale-gen sv_SE.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Install PHPUnit 4.8 for PHP 5.5  
RUN wget https://phar.phpunit.de/phpunit-old.phar  
RUN chmod +x phpunit-old.phar  
RUN mv phpunit-old.phar /usr/local/bin/phpunit  
  
# Install PHPMetrics  
RUN wget
https://github.com/phpmetrics/PhpMetrics/raw/master/build/phpmetrics.phar  
RUN chmod +x phpmetrics.phar  
RUN mv phpmetrics.phar /usr/local/bin/phpmetrics  
  
# Install aws-cli  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"  
RUN python get-pip.py  
RUN pip install --upgrade --user awscli  
RUN export PATH=~/.local/bin:$PATH  
RUN touch ~/.bash_profile  
RUN /bin/bash -c "source ~/.bash_profile"  
  
# Set default volume for image  
# This would be overrided by docker-compose for updatable source code between
development  
COPY . /data  
WORKDIR /data  
  
# Fixes user permissions for Mac OS
[https://github.com/boot2docker/boot2docker/issues/581]  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
# Setup cronjob for Indatus/dispatcher  
RUN crontab -l | { cat; echo "* * * * * cd /data && php artisan scheduled:run
1>> /dev/null 2>&1"; } | crontab -  
  
# Supervisor setup for queue process  
ADD supervisor-laravel-queue.conf /etc/supervisor/conf.d/supervisord-laravel-
queue.conf  
  
CMD ["/run.sh"]

