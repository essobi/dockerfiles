FROM php:5.6-cli  
  
MAINTAINER Kazuki Yamaguchi  
  
#update repo  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
curl \  
git \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
#Download dependencies  
# Set memory limit  
RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini  
  
# Set environmental variables  
ENV COMPOSER_HOME /root/composer  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN docker-php-ext-install \  
zip \  
bz2 \  
iconv \  
mcrypt \  
mbstring \  
pdo_mysql  
  
# Install package for ruby  
RUN apt-get install -y \  
zlib1g-dev \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libxml2-dev \  
libxslt-dev  
  
# Install package for sqlite3  
RUN apt-get install -y \  
sqlite3 \  
libsqlite3-dev  
  
# Install package for postgresql  
RUN apt-get install -y libpq-dev  
  
# Install ruby-build  
RUN git clone https://github.com/sstephenson/ruby-build.git .ruby-build  
RUN .ruby-build/install.sh  
RUN rm -fr .ruby-build  
  
# Install ruby-2.1.2  
RUN ruby-build 2.1.2 /usr/local  
  
# Install bundler  
RUN gem update --system  
RUN gem install bundler --no-rdoc --no-ri  
  
CMD ["php"]  
CMD ["irb"]  

