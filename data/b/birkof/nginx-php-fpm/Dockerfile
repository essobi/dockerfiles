FROM alpine:3.4  
  
MAINTAINER birkof <docker@birkof.ro>  
  
ENV TERM=xterm  
ENV TZ=Europe/London  
ENV SHELL=/bin/zsh  
  
# Install packages  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& echo http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache \  
bash \  
zsh \  
tzdata \  
wget \  
curl \  
vim \  
git \  
openssh-client \  
supervisor \  
nginx \  
php5 \  
php5-common \  
php5-cli \  
php5-fpm \  
php5-pdo \  
php5-pdo_mysql \  
php5-mysql \  
php5-mysqli \  
php5-mcrypt \  
php5-ctype \  
php5-zlib \  
php5-gd \  
php5-intl \  
php5-memcache \  
php5-sqlite3 \  
php5-pgsql \  
php5-xml \  
php5-xsl \  
php5-curl \  
php5-openssl \  
php5-iconv \  
php5-json \  
php5-phar \  
php5-soap \  
php5-dom \  
php5-zip \  
php5-xdebug \  
python \  
python-dev \  
py-pip \  
augeas-dev \  
openssl-dev \  
ca-certificates \  
dialog \  
gcc \  
musl-dev \  
linux-headers \  
libffi-dev \  
&& apk del \  
gcc \  
musl-dev \  
linux-headers \  
libffi-dev \  
augeas-dev \  
python-dev \  
&& rm -rf /var/cache/apk/* \  
&& find / -type f -iname \\*.apk-new -delete  
# Install composer  
RUN curl -LsS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer --version  
  
# Install PhpUnit  
RUN curl -LsS https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit \  
&& chmod a+x /usr/local/bin/phpunit \  
&& phpunit --version  
  
# Installing “Oh My ZSH!”  
RUN sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"  
# Necesary resources  
RUN mkdir -p /etc/nginx/sites-enabled /etc/nginx/ssl /var/log/supervisor
/run/nginx \  
&& rm -Rf /var/www/* \  
&& mkdir -p /var/www/html  
  
# Nginx default vhost file  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Injecting s assets files  
ADD .docker /  
  
# Injecting container bootstrap file  
RUN mv /bootstrap.sh /usr/local/bin/bootstrap \  
&& chmod +x /usr/local/bin/bootstrap  
  
# Working dir  
WORKDIR /var/www/html  
  
# Volume mounting  
VOLUME /var/www/html  
  
# Exposed ports  
EXPOSE 443 80  
  
CMD ["bootstrap"]

