FROM debian:stretch  
MAINTAINER Rodrigue Villetard <rodrigue@villetard.tech>  
  
RUN apt update \  
&& apt install -y curl wget apt-transport-https lsb-release ca-certificates \  
&& curl https://packages.sury.org/php/apt.gpg > /etc/apt/trusted.gpg.d/php.gpg
\  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt update \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc  
  
RUN apt-get update && apt-get install -y \  
git \  
imagemagick \  
libgl1-mesa-glx \  
libsm6 \  
libxrender-dev \  
mysql-client \  
php7.2-cli \  
php7.2-imagick \  
php7.2-curl \  
php7.2-dom \  
php7.2-gd \  
php7.2-intl \  
php7.2-json \  
php7.2-mbstring \  
php7.2-mysql \  
php7.2-pgsql \  
php7.2-sqlite3 \  
php7.2-xsl \  
php7.2-zip \  
ssmtp \  
unzip \  
vim \  
xfonts-base \  
xfonts-75dpi \  
zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc  
  
COPY ./install-composer.sh /root/  
  
RUN /bin/bash /root/install-composer.sh \  
&& composer global require hirak/prestissimo friendsofphp/php-cs-fixer  
  
RUN wget "https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb" -q -O /opt/chrome.deb \  
&& apt update && apt install -y /opt/chrome.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc  
  
WORKDIR /app  
  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/.composer/vendor/bin:/app/vendor/bin  
  

