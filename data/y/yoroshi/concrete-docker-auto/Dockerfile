FROM chriswayg/apache-php  
MAINTAINER Drew Hutton  
  
# This image provides Concrete5.8.3.2 at root of site  
# Install pre-requisites for Concrete5 & nano for editing conf files  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
php5-curl \  
php5-gd \  
php5-mysql \  
unzip \  
wget \  
patch \  
git-all \  
nano && \  
apt-get clean && rm -r /var/lib/apt/lists/*  
  
# Find latest download details at https://www.concrete5.org/get-started  
# - for newer version: change Concrete5 version# & download url & md5  
ENV CONCRETE5_VERSION 5-8.3.2  
ENV C5_URL http://www.concrete5.org/download_file/-/view/100595/8497/  
ENV C5_MD5 4025fa119449c435a404f5dbdc8ed0a8  
# nano and other commands will not work without this  
ENV TERM xterm  
# Variable for production mode (For when the data is not saved in the same
folder and or in production environment and want to update the site solely
with git updates  
ENV PRODUCTION_MODE true  
  
# Copy apache2 conf dir & Download Concrete5  
# Perl script to enable ability to activate 'Pretty URLs' and redirection in
.htaccess by 'AllowOverride'  
# - it matches a multi-line string and replaces 'None' with 'FileInfo'  
RUN perl -i.bak -0pe 's/<Directory \/var\/www\/>\n\tOptions Indexes
FollowSymLinks\n\tAllowOverride None/<Directory \/var\/www\/>\n\tOptions
Indexes FollowSymLinks\n\tAllowOverride FileInfo/' /etc/apache2/apache2.conf
&& \  
cp -r /etc/apache2 /usr/local/etc/apache2 && \  
cd /usr/local/src && \  
wget --no-verbose $C5_URL -O concrete5.zip && \  
echo "$C5_MD5 concrete5.zip" | md5sum -c - && \  
unzip -qq concrete5.zip && \  
rm -v concrete5.zip && \  
rm -v /var/www/html/index.html  
  
# Persist website user data, logs & apache config  
VOLUME [ "/var/www/html", "/var/log/apache2", "/etc/apache2" ]  
  
EXPOSE 80 443  
WORKDIR /var/www/html  
  
COPY docker-entrypoint /docker-entrypoint  
  
ENTRYPOINT ["/docker-entrypoint"]  
CMD ["apache2-foreground"]  

