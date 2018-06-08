FROM ubuntu:16.04  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install apache2 -y \  
&& apt-get install -y software-properties-common python-software-properties \  
&& echo '\n' | LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y php7.1 php7.1-xml php7.1-mbstring php7.1-mysql
php7.1-json php7.1-curl php7.1-cli php7.1-common php7.1-mcrypt php7.1-gd
libapache2-mod-php7.1 php7.1-zip \  
&& apt-get install curl \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& chmod -R 777 /var/www/html/  
WORKDIR /var/www/html/  
RUN useradd -r user \  
&& composer create-project laravel/laravel NmapWeb \--prefer-dist \  
&& chmod -R 777 /var/www/html/NmapWeb/  
USER root  
EXPOSE 80  
ENTRYPOINT [ "/bin/bash" ]  

