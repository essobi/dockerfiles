FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
sudo \  
ntp \  
net-tools \  
telnet \  
git \  
gnupg2 \  
curl \  
apt-utils \  
daemon  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-add-repository -y ppa:nginx/stable \  
&& apt-get update \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN add-apt-repository -y ppa:ondrej/php \  
&& apt-get update  
  
RUN apt-get update && apt-get install -y --force-yes \  
sudo \  
ntp \  
net-tools \  
telnet \  
git \  
curl \  
daemon \  
php \  
pkg-php-tools \  
gnupg2 \  
dh-php \  
php-pear \  
php7.0-apcu \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-dev \  
php7.0-fpm \  
php7.0-gd \  
php7.0-gmp \  
php7.0-imap \  
php7.0-json \  
php7.0-mcrypt \  
php7.0-memcached \  
php7.0-mysqlnd \  
php7.0-pgsql \  
php7.0-readline \  
php7.0-sqlite \  
php7.0-xdebug  
  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | sudo bash
-  
RUN apt-get install --yes nodejs  
RUN apt-get install --yes build-essential  
RUN npm install -g bower -y  
RUN npm install -g grunt  
RUN npm install -g grunt-cli  
  
RUN groupadd -r dateperfect && useradd -r -g dateperfect dateperfect  
RUN groupadd -r nginx && useradd -r -g nginx nginx  
RUN chmod -R 775 /etc/nginx/sites-available && chown -R dateperfect:nginx
/etc/nginx/sites-available  
RUN chmod -R 775 /etc/nginx/sites-enabled && chown -R dateperfect:nginx
/etc/nginx/sites-enabled  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

