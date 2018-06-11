FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apache2 \  
php7.0 \  
libapache2-mod-php7.0 \  
php7.0-cli \  
php7.0-common \  
php7.0-mbstring \  
php7.0-gd \  
php7.0-intl \  
php7.0-xml \  
php7.0-mysql \  
php7.0-mcrypt \  
php7.0-zip \  
git \  
gcc \  
curl \  
&& rm -r /var/lib/apt/lists/*  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
WORKDIR /tmp  
  
COPY composer-setup.php composer-setup.php  
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer  
  
RUN a2enmod rewrite \  
&& a2enmod headers  
COPY apache.conf /etc/apache2/sites-available/000-default.conf  
  
RUN ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY start-container /usr/local/bin/start-container  
RUN chmod +x /usr/local/bin/start-container  
  
EXPOSE 80  
CMD ["start-container"]

