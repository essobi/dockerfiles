FROM debian:stretch  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https lsb-release ca-certificates wget \  
&& wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& echo "deb-src http://packages.sury.org/php/ $(lsb_release -sc) main" >>
/etc/apt/sources.list.d/php.list \  
&& apt-get update --fix-missing  
  
RUN adduser --system \  
\--uid 1000 \  
\--group \  
\--home /var/lib/php \  
\--no-create-home \  
\--shell /usr/sbin/nologin \  
\--disabled-login \  
\--gecos 'PHP FastCGI Process Manager' php  
  
RUN apt-get install -y --fix-missing \  
pkg-config libssl-dev \  
git \  
curl \  
zip \  
php7.1-cli \  
php7.1-mysql \  
php7.1-sqlite3 \  
php7.1-apcu \  
php7.1-fpm \  
php7.1-mbstring \  
php7.1-zip \  
php7.1-dev \  
&& apt-get update --fix-missing \  
&& apt-get autoremove \  
&& apt-get clean  
  
# Install php extensions: GD, xml  
RUN apt-get update && apt-get install -y --fix-missing php7.1-gd php7.1-xml  
  
RUN curl --silent https://getcomposer.org/installer | php  
RUN cp composer.phar /usr/bin/composer  
  
WORKDIR /app  
COPY . /app  
  
RUN cp /app/docker/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
  
CMD /usr/sbin/php-fpm7.1 -F -O 2>&1  

