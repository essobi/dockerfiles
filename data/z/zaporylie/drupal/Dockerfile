FROM ubuntu:trusty  
MAINTAINER Jakub Piasecki <jakub@piaseccy.pl>  
  
VOLUME ["/app"]  
WORKDIR /app  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get -yq install \  
openssh-server \  
supervisor \  
php5-mysql \  
mysql-client \  
git \  
curl \  
nginx \  
php5-fpm \  
unzip \  
php5-curl \  
php5-gd \  
php-pear \  
php-apc \  
mysql-server \  
php5-mysql \  
shunit2 \  
pwgen \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN echo 'efuwyg' && composer global require drush/drush:dev-master \  
&& echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc  
  
COPY ./conf /root/conf/  
  
RUN sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/fpm/php.ini \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i -e "s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf \  
&& sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini \  
&& sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf \  
&& find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \; \  
&& cp /root/conf/drupal.conf /etc/nginx/sites-available/default \  
&& sed -ri 's/^expose_php\s*=\s*On/expose_php = Off/g' /etc/php5/fpm/php.ini \  
&& sed -ri 's/^expose_php\s*=\s*On/expose_php = Off/g' /etc/php5/cli/php.ini \  
&& sed -ri 's/^allow_url_fopen\s*=\s*On/allow_url_fopen = Off/g'
/etc/php5/fpm/php.ini \  
&& sed -ri 's/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 64M/g'
/etc/php5/fpm/php.ini \  
&& sed -ri 's/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 64M/g'
/etc/php5/cli/php.ini \  
&& mkdir -p /var/run/nginx /var/run/sshd /var/log/supervisor \  
&& cp /root/conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf \  
&& mkdir -p /var/run/sshd \  
&& echo 'root:defaultpassword' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& echo "export VISIBLE=now" >> /etc/profile  
  
ENV DRUPAL_PROFILE=minimal \  
DRUPAL_SUBDIR=default  
  
ENV CODE_SYNC_METHOD=auto \  
CODE_SYNC_FOLDER=/app/drupal  
ENV CODE_DRUSH_MAJOR_VERSION=8  
ENV CODE_GIT_CLONE_URL=http://git.drupal.org/project/drupal.git \  
CODE_GIT_CLONE_BRANCH=8.0.x \  
CODE_GIT_CLONE_DEPTH=1 \  
CODE_GIT_SHA=HEAD  
  
ENV DB_SYNC_METHOD=auto \  
DB_SYNC_FILE=/app/backup/backup.sql  
ENV DB_HOSTNAME=db \  
DB_USER=drupal \  
DB_PASSWORD=drupal \  
DB_NAME=drupal  
  
ENV TEST_BUILD= \  
TEST_DRUPAL=  
  
ENV NOTVISIBLE="in users profile"  
  
EXPOSE 22 80  
  
ENTRYPOINT ["/bin/bash"]  
  
CMD ["/root/conf/run.sh"]  

