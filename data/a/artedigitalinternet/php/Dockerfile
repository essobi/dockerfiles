FROM php:5.6-apache  
  
RUN apt-get update \  
&& apt-get install -y \  
zip \  
unzip \  
wget \  
curl \  
git \  
imagemagick \  
&& rm -rf /var/lib/apt/lists/*  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# soap  
RUN buildRequirements="libxml2-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install soap \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# zip  
RUN buildRequirements="zlib1g-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install zip \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# gd  
RUN buildRequirements="libpng12-dev libjpeg-dev libfreetype6-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
# mysqli  
RUN docker-php-ext-install mysqli  
  
# mcrypt  
RUN runtimeRequirements="re2c libmcrypt-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install mcrypt \  
&& rm -rf /var/lib/apt/lists/*  
# mbstring  
RUN docker-php-ext-install mbstring  
  
# intl  
RUN buildRequirements="libicu-dev g++" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install intl \  
&& apt-get purge -y ${buildRequirements} \  
&& runtimeRequirements="libicu52" \  
&& apt-get install -y --auto-remove ${runtimeRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# imagick  
RUN runtimeRequirements="libmagickwand-6.q16-dev --no-install-recommends" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin/ \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& rm -rf /var/lib/apt/lists/*  
# opcache  
RUN docker-php-ext-install opcache  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
COPY conf/php.ini /usr/local/etc/php/  
COPY conf/apache.conf /etc/apache2/sites-available/000-default.conf  
  
RUN a2enmod rewrite  
  
WORKDIR /var/www  

