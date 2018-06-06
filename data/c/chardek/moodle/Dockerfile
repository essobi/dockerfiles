FROM ubuntu:trusty  
MAINTAINER Chris Hardekopf <chrish@basis.com>  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Get all the packages to run Moodle  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install mysql-client pwgen python-setuptools curl git unzip apache2
php5 \  
php5-gd libapache2-mod-php5 postfix wget supervisor php5-pgsql curl libcurl3 \  
libcurl3-dev php5-curl php5-xmlrpc php5-intl php5-cgi php5-mysql git-core zip
openssl  
  
# Remove DEFAULT apache site  
RUN rm -rf /var/www/html  
  
# Download 2.8.X release of Moodle uncomment when Elegance theme is released
for version 2.8.X  
ADD https://download.moodle.org/download.php/direct/stable28/moodle-2.8.5.zip
/tmp/  
RUN unzip /tmp/moodle-2.8.5.zip -d /var/www/ && rm -f /tmp/moodle-2.8.5.zip  
  
# Download and install the moodle 2.8 Course Enrolment upon Approval plugin  
ADD
https://moodle.org/plugins/download.php/7797/enrol_apply_moodle28_2015012500.zip
/tmp/  
RUN unzip /tmp/enrol_apply_moodle28_2015012500.zip -d /var/www/moodle/enrol/
&& \  
rm -f /tmp/enrol_apply_moodle28_2015012500.zip  
  
# symlink moodle install dir to html  
RUN ln -s /var/www/moodle /var/www/html  
  
# Download theme bootstrap for moodle 2.8.X uncomment when Elegance theme is
released for version 2.8.X  
ADD
https://moodle.org/plugins/download.php/7472/theme_bootstrap_moodle28_2014120803.zip
/tmp/  
RUN unzip /tmp/theme_bootstrap_moodle28_2014120803.zip -d
/var/www/moodle/theme/ && \  
rm -f /tmp/theme_bootstrap_moodle28_2014120803.zip  
  
# Download Elegance theme for Moodle 2.7.X  
ADD
https://moodle.org/plugins/download.php/6707/theme_elegance_moodle27_2014082100.zip
/tmp/  
RUN unzip /tmp/theme_elegance_moodle27_2014082100.zip -d
/var/www/moodle/theme/ && \  
rm -f /tmp/theme_elegance_moodle27_2014082100.zip  
  
# Copy current moodle conf to apache site available  
ADD moodle.conf /etc/apache2/sites-available/  
WORKDIR /var/www/html  
  
# Chown Moodle file to www-data  
RUN chown -R www-data:www-data /var/www/html  
  
# Enable Moodle site and Disable default apache site  
RUN a2enmod php5 ssl && a2ensite moodle && a2dissite 000-default  
  
# copy existing moodle config  
# COPY config.php /var/www/html/config.php  
# Expose web server port  
EXPOSE 80  
# Add the start script  
ADD start /opt/  
  
# Change start to executable  
RUN chmod a+x /opt/start  
  
# Run start script  
CMD ["/opt/start"]  

