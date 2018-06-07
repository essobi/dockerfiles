FROM ubuntu:latest  
MAINTAINER Ron Williams <hello@ronwilliams.io>  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN apt-get update  
RUN apt-get install -y wget tmux vim build-essential software-properties-
common  
RUN add-apt-repository -y ppa:ondrej/php5-5.6  
RUN apt-get install -y apache2 php-pear php5-curl php5-mysql php5-odbc
php5-imagick php5-mcrypt php5-fpm mysql-client curl git libsasl2-modules
rsyslog python-setuptools libapache2-mod-php5 php5-imap  
RUN apt-get install -y imagemagick php5-imagick php5-gd  
RUN pear install Mail Mail_Mime Net_SMTP Net_Socket Spreadsheet_Excel_Writer
XML_RPC  
RUN php5enmod mcrypt  
  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
RUN a2enmod rewrite  
RUN a2enmod php5  
  
RUN rm -f /etc/apache2/sites-available/000-default.conf  
  
ADD conf/supervisord.conf /etc/supervisord.conf  
ADD conf/website.conf /etc/apache2/sites-available/000-default.conf  
ADD conf/httpd.conf /etc/apache2/apache2.conf  
ADD conf/php.ini /etc/php5/apache2/php.ini  
ADD conf/rsyslog.conf /etc/rsyslog.conf  
ADD conf/lamp.sh /etc/lamp.sh  
  
RUN chmod +x /etc/lamp.sh  
  
# Add admin scripts to directory  
COPY conf/tools/ /usr/local/share/lap-docker/  
  
# Install Pimp My Logs  
RUN git clone https://github.com/potsky/PimpMyLog.git /usr/local/share/lap-
docker/logs/  
ADD conf/pimpmylog/pimpmylog.ini /etc/php5/conf.d/pimpmylog.ini  
RUN cd /etc/php5/cli/conf.d && ln -s ../../conf.d/pimpmylog.ini pimpmylog.ini
&&\  
cd /etc/php5/apache2/conf.d && ln -s ../../conf.d/pimpmylog.ini pimpmylog.ini  
# Allows apache to read log files directly  
RUN usermod -G adm www-data  
# Creates initial php error log  
RUN touch /var/log/apache2/php.err  
# Creates default configuration file  
ADD conf/pimpmylog/config.user.php /usr/local/share/lap-
docker/logs/config.user.php  
  
# Fix session write warnings  
RUN chown www-data:www-data /var/lib/php5  
RUN chmod g+rwx /var/lib/php5  
  
RUN apachectl configtest  
RUN rm -rf /var/www  
  
# Install Mailcatcher Dependencies (sqlite, ruby)  
RUN apt-get install -y libsqlite3-dev ruby1.9.1-dev  
  
# Install Mailcatcher as a Ruby gem  
RUN gem install mailcatcher --no-rdoc --no-ri  
ADD conf/mailcatcher.upstart /etc/init.d/mailcatcher  
  
# Install drush for Drupal Development  
RUN apt-get install -y drush  
  
# Install Bundler and Theme related tweaks  
RUN gem install bundler  
RUN export LC_ALL="C.UTF-8"  
  
# Install Mailcatcher php configuration  
ADD conf/mailcatcher.ini /etc/php5/conf.d/mailcatcher.ini  
RUN cd /etc/php5/cli/conf.d && ln -s ../../conf.d/mailcatcher.ini
mailcatcher.ini &&\  
cd /etc/php5/apache2/conf.d && ln -s ../../conf.d/mailcatcher.ini
mailcatcher.ini  
  
RUN service apache2 stop  
RUN service rsyslog stop  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/etc/lamp.sh"]  

