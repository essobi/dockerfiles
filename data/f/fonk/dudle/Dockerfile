# docker container running dudle  
FROM debian:jessie  
MAINTAINER Frank Grötzner <frank@unforgotten.de>  
  
# set needed variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
  
# install dudle  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --force-yes --no-install-recommends \  
apache2 \  
# for dudle  
ruby git \  
ruby-gettext \  
# for locales  
potool make gettext locales \  
# for atom-feed  
rubygems ruby-dev libxml2-dev zlib1g-dev  
  
# add apache configuration  
ADD etc/apache2/sites-available /etc/apache2/sites-available  
  
# generate locales  
RUN echo en_US.UTF-8 UTF-8 >> /etc/locale.gen && locale-gen  
  
# install dudle and configure apache  
RUN cd /var/www/html && \  
git clone https://github.com/kellerben/dudle.git && \  
chown www-data dudle && \  
cd dudle && \  
LC_ALL=en_US.utf8 make && \  
a2dissite 000-default && \  
a2ensite 001-dudle && \  
a2enmod cgid && \  
a2enmod auth_digest && \  
a2enmod rewrite  
  
# configure some needed parameters  
RUN echo 'SetEnv RUBYLIB /var/www/html/dudle' >> /var/www/html/dudle/.htaccess
&& \  
echo 'SetEnv RUBYOPT "-E UTF-8:UTF-8"' >> /var/www/html/dudle/.htaccess && \  
echo 'SetEnv GIT_AUTHOR_NAME="http user"' >> /var/www/html/dudle/.htaccess &&
\  
echo 'SetEnv GIT_AUTHOR_EMAIL=foo@example.org' >>
/var/www/html/dudle/.htaccess && \  
echo 'SetEnv GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"' >>
/var/www/html/dudle/.htaccess && \  
echo 'SetEnv GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"' >>
/var/www/html/dudle/.htaccess  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
VOLUME [ "/var/www/html/dudle" ]  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

