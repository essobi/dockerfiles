FROM ubuntu:xenial  
  
MAINTAINER Joachim Wickman <joachim@wickman.in>  
  
EXPOSE 80 443  
ENV ROUNDCUBE_VERSION 1.2.5  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && \  
apt-get dist-upgrade -qq -y && \  
apt-get install -y nano \  
# install requirements  
apache2 libapache2-mod-php7.0 \  
php7.0 php7.0-cli php7.0-mysql php7.0-mcrypt php7.0-intl php7.0-mbstring
php7.0-ldap \  
ca-certificates php-pear && \  
# install Pear requirements  
pear install mail_mime mail_mimedecode net_smtp net_idna2-beta auth_sasl
net_sieve crypt_gpg && \  
# cleanup  
apt-get clean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# host Configuration  
COPY mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf  
COPY 000-roundcube.conf /etc/apache2/sites-available/000-roundcube.conf  
  
RUN rm /etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/* && \  
a2ensite 000-roundcube.conf && \  
a2enmod deflate rewrite expires headers php7.0  
  
# install code from git  
RUN apt-get update && \  
apt-get install -y git && \  
rm -rf /var/www/html/* && \  
cd /var/www/html && git clone https://github.com/roundcube/roundcubemail.git .
&& \  
git checkout tags/$ROUNDCUBE_VERSION && rm -rf installer .git && \  
# cleanup  
apt-get remove -y git && apt-get clean -y && apt-get -y autoremove && rm -rf
/var/lib/apt/lists/*  
  
# app configuration  
RUN . /etc/apache2/envvars && chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP}
/var/www/html/temp /var/www/html/logs  
COPY config.inc.php /var/www/html/config/config.inc.php  
  
# add bootstrap tool  
ADD bootstrap.php /  
  
ADD entry.sh /  
ENTRYPOINT ["/entry.sh"]  
CMD [ "/usr/sbin/apache2ctl", "-D", "FOREGROUND", "-k", "start" ]  

