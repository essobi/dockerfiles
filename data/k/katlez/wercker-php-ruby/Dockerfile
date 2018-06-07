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
  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.4  
ENV RUBY_DOWNLOAD_SHA256
b6eff568b48e0fda76e5a36333175df049b204e91217aa32a65153cc0cdcb761  
ENV RUBYGEMS_VERSION 2.5.1  
# skip installing gem documentation  
RUN echo 'install: --no-document\nupdate: --no-document' >> "$HOME/.gemrc"  
  
RUN apt-get -y install \  
build-essential \  
libcurl4-openssl-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
g++ \  
flex \  
gperf \  
ruby \  
perl \  
libsqlite3-dev \  
libfontconfig1-dev \  
libicu-dev \  
libpng-dev \  
libjpeg-dev \  
python \  
libx11-dev \  
libxext-dev  
  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN apt-get install -y bison libgdbm-dev ruby \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/ruby \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& apt-get purge -y --auto-remove bison libgdbm-dev ruby \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
ENV BUNDLER_VERSION 1.11.2  
RUN gem install bundler --version "$BUNDLER_VERSION" \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin" \  
&& bundle config --global silence_root_warning true  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
ENV COMPOSER_VERSION 1.0.0-alpha11  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}  
  
# Display version information  
RUN composer --version  
  
CMD ["php"]  

