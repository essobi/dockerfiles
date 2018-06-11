FROM alpine:3.7  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0"  
  
ENV YHM_HOST=1  
RUN apk add --no-cache \  
apache2 curl git mysql-client patch \  
php7 php7-apache2 php7-bcmath php7-bz2 php7-ctype php7-curl php7-dom php7-gd
php7-json php7-mbstring php7-opcache php7-openssl php7-pdo php7-pdo_mysql
php7-phar php7-session php7-simplexml php7-tokenizer php7-xml php7-xmlwriter
php7-zip php7-zlib \  
python rsync && \  
mkdir -p /run/apache2 && mkdir -p /opt/utils  
  
# Install composer.  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php --install-dir=bin --filename=composer && \  
rm composer-setup.php && \  
echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> /etc/profile && \  
composer global require hirak/prestissimo && \  
curl -L -o /usr/local/bin/drush https://github.com/drush-ops/drush-
launcher/releases/download/0.4.2/drush.phar && \  
chmod 755 /usr/local/bin/drush  
  
# Install s3cmd.  
RUN curl -L -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install python-dateutil s3cmd  
ADD s3cmd-config /root/.s3cfg  
  
ADD start.sh /opt/utils  
RUN chmod +x /opt/utils/start.sh  
  
VOLUME /files  
  
EXPOSE 80  
ENTRYPOINT ["/opt/utils/start.sh"]  

