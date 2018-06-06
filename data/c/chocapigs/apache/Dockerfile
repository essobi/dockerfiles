FROM silintl/ubuntu:16.04  
MAINTAINER Sébastien TRYBUS <strybus@nextoo.fr>  
  
ENV REFRESHED_AT 2016-04-22  
ENV HTTPD_PREFIX /etc/apache2  
  
# install OS packages  
RUN apt-get update && apt-get install -y \  
apache2 \  
curl \  
git \  
libapache2-mod-php \  
netcat \  
php \  
php-cli \  
php-curl \  
php-dom \  
php-intl \  
php-json \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-zip \  
php-pgsql \  
php-imagick \  
php-xdebug \  
php-gd \  
vim \  
  
s3cmd \  
rsyslog-gnutls \  
&& phpenmod mcrypt \  
&& apt-get clean  
  
RUN a2enmod rewrite  
  
# Blackfire  
#RUN curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/55\  
# && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
# && mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so \  
# && echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}"
> /etc/php5/apache2/conf.d/blackfire.ini  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
WORKDIR /data  
ENV HOME=/data  
RUN npm install -g bower grunt-cli && npm set cache /data/.npm --global  
  
RUN apt-get install ruby -y  
RUN gem install sass  
  
# Add image configuration and scripts  
ADD apache.sh /apache.sh  
RUN chmod 755 /*.sh  
  
# Run the command on container startup  
CMD cron && tail -f /var/log/cron.log  
  
#Create Log repo  
RUN mkdir /var/log/apache2/api/  
  
EXPOSE 80  
CMD ["/apache.sh"]  

