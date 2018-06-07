FROM bitnami/minideb:jessie  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Repository updates and upgrades  
RUN install_packages \  
wget \  
curl \  
cron \  
locales \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
git \  
apache2  
  
# Timezone and locales  
ENV TZ "Europe/Paris"  
ENV LANGUAGE "fr_FR"  
ENV LANG "${LANGUAGE}.UTF-8"  
ENV LC_ALL ${LANG}  
  
RUN echo "${LANG} UTF-8" > /etc/locale.gen && \  
locale-gen ${LANG} && \  
dpkg-reconfigure locales && \  
/usr/sbin/update-locale LANG=${LANG}  
  
RUN echo ${TZ} > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# deb.sury.org  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
RUN echo "deb https://packages.sury.org/php/ jessie main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update  
  
# PHP 7 installation  
RUN install_packages \  
php7.1 \  
php7.1-cli \  
libapache2-mod-php7.1 \  
php7.1-mysql \  
php7.1-gd \  
php7.1-mbstring \  
php7.1-curl \  
php7.1-xmlwriter \  
php7.1-zip \  
php7.1-json \  
php7.1-xdebug  
  
# PHP configuration  
RUN echo "date.timezone=$TZ" >> /etc/php/7.1/cli/php.ini  
RUN echo "date.timezone=$TZ" >> /etc/php/7.1/apache2/php.ini  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Environment  
ENV VOLUME_UID 1000  
ENV APACHE_DOCUMENTROOT /var/www  
  
# Apache configuration  
RUN sed -i 's/DocumentRoot\ \/var\/www\/html/DocumentRoot\
\$APACHE_DOCUMENTROOT/g' /etc/apache2/sites-enabled/000-default.conf  
RUN echo "ServerName dev" >> /etc/apache2/apache2.conf && \  
a2enmod rewrite vhost_alias headers expires  
  
# Alias  
RUN echo 'alias ll="ls -lah --color"' >> ~/.bashrc  
RUN echo 'alias ll="ls -lah --color"' >> /var/www/.bashrc  
  
# Mailhog  
RUN curl -Lsf 'https://storage.googleapis.com/golang/go1.8.3.linux-
amd64.tar.gz' | tar -C '/usr/local' -xvzf -  
ENV PATH /usr/local/go/bin:$PATH  
RUN go get github.com/mailhog/mhsendmail  
RUN cp /root/go/bin/mhsendmail /usr/bin/mhsendmail  
RUN echo 'sendmail_path = /usr/bin/mhsendmail --smtp-addr mailhog:1025' >
/etc/php/7.1/apache2/php.ini  
  
# Cleanup  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Start script  
EXPOSE 80  
ADD ./start.sh /usr/bin/start  
RUN chmod 0755 /usr/bin/start  
CMD ["bash", "start"]  

