FROM phusion/baseimage  
MAINTAINER Terence Kent <tkent@xetus.com>  
  
#  
# Install all the pre-reqs for owncloud, according to their documentation  
#  
RUN apt-get update &&\  
apt-get install -y apache2 apache2-utils libapache2-mod-fcgid\  
libapache2-mod-php5 php5-apcu php5-ldap php5-mysql php5-pgsql\  
php5-sqlite php5-imagick php5-curl php5-intl php5-json php5-gd\  
php-net-ftp smbclient php5-mcrypt openssl &&\  
php5enmod mcrypt && sudo a2enmod ssl && a2enmod rewrite  
  
#  
# Go get the owncloud version we'll installing  
#  
RUN OWNCLOUD_VERSION="8.1.4" &&\  
cd /tmp &&\  
curl -O
https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2
&&\  
cd /opt && tar xjf /tmp/owncloud-${OWNCLOUD_VERSION}.tar.bz2  
  
ADD autoconfig.php /opt/owncloud/config/autoconfig.php  
ADD apache-owncloud.conf /etc/apache2/conf-enabled/owncloud.conf  
  
#  
# Adjust ownership and do the baseline perms for security  
#  
RUN cd /opt && chown -R www-data:www-data owncloud &&\  
find owncloud -type d -exec chmod 750 {} \; &&\  
find owncloud -type f -exec chmod 640 {} \;  
#  
# Do system level configuration tweaks  
#  
RUN echo 'default_charset = UTF-8' >> /etc/php5/apache2/conf.d/charset.ini  
  
#  
# Perform the data directory initialization  
#  
ADD data_dirs.env /data_dirs.env  
ADD init.bash /init.bash  
# Sync calls are due to https://github.com/docker/docker/issues/9547  
RUN cd / && chmod 755 /init.bash &&\  
sync && /init.bash &&\  
sync && rm /init.bash  
  
#  
# Add the bootstrap cmd  
#  
ADD run.bash /run.bash  
RUN chmod 755 /run.bash  
  
#  
# All data is stored on the root data volume. The expected directories are:
config, data, apps, dotfiles  
#  
VOLUME ["/owncloud-data"]  
  
# Standard web ports exposted  
EXPOSE 80/tcp 443/tcp  
  
ENTRYPOINT ["/run.bash"]  

