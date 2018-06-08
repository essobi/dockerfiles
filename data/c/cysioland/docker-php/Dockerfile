FROM php:7.2.5-cli  
ADD install-composer.sh /tmp/  
ADD .profile /root/  
RUN apt-get update && apt-get install -y gnupg \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update && apt-get install -y zlib1g-dev libsqlite3-dev build-
essential nodejs git wget coreutils libsodium-dev \  
&& docker-php-ext-install -j$(nproc) zip pdo_mysql pdo_sqlite \  
&& /tmp/install-composer.sh \  
&& echo 'export PATH=/root/.config/composer/vendor/bin:$PATH' >>
/root/.profile \  
&& npm -g install gulp-cli bower \  

