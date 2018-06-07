FROM debian:jessie  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y apache2 curl php5 git vim php5-mcrypt php5-mysql mysql-
client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DEPLOY_PATH /var/www/auth  
RUN git clone https://github.com/ucla/shib-oauth2-bridge.git "$DEPLOY_PATH"  
  
WORKDIR $DEPLOY_PATH  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& php composer.phar install --prefer-source  
  
ADD auth.conf /etc/apache2/sites-available/000-auth.conf  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf \  
&& ln -s /etc/apache2/sites-available/000-auth.conf /etc/apache2/sites-
enabled/ \  
&& a2enmod rewrite  
  
RUN sed -i 's/#SetEnv/SetEnv/g' /var/www/auth/public/.htaccess  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh \  
&& chown -R www-data.www-data /var/www/auth  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
EXPOSE 80  
CMD ["/run.sh"]

