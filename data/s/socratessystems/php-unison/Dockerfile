FROM php:7.1-fpm  
  
RUN ln -s /unison /opt/app && \  
apt-get update && apt-get install -y \  
libmcrypt-dev \  
libpq-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libxml2-dev \  
zlib1g-dev \  
g++ \  
&& docker-php-ext-install -j$(nproc) mcrypt pdo_pgsql zip xml soap intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN apt-get install -y xfonts-base xfonts-75dpi xfonts-utils xfonts-encodings
libxfont1 libfontenc1 fontconfig libfreetype6 libx11-6 libxext6 libxrender1
gsfonts wget libxrender-dev gdebi  
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin  
RUN rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
  
WORKDIR /opt/app  

