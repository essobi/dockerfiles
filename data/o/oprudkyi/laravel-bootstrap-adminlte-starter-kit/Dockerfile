FROM php:7.0  
  
# this image adds additional software to default php image  
# to allow ci tests run faster  
#  
# additional software :  
# - php extentions : mcrypt zip pdo_mysql opcache gd memcached  
# - nodejs/npm  
# - ruby/gem  
# - autotools (automake/autoconf)  
# - phnatomjs (headless webbrowser for testing)  
# - git/wget/curl etc  
  
  
MAINTAINER Oleksii Prudkyi <oleksii.prudkyi@gmail.com>  
  
RUN apt-get update -yqq \  
&& apt-get install -y curl \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& buildDeps=" \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libmcrypt-dev \  
" \  
&& doNotUninstall=" \  
libmemcached11 \  
libmemcachedutil2 \  
libfreetype6 \  
libhashkit2 \  
libjpeg62-turbo \  
libmcrypt4 \  
libpng12-0 \  
libpq5 \  
autotools-dev \  
fontconfig-config fonts-dejavu-core \  
icu-devtools krb5-multidev liberror-perl \  
libgmpxx4ldbl libgssrpc4 \  
libicu52 libkadm5clnt-mit9 libkadm5srv-mit9 libkdb5-7 \  
libpsl0 libruby2.1 libyaml-0-2 ruby2.1 ruby2.1-dev rubygems-integration ucf \  
krb5-multidev libgssrpc4 \  
" \  
&& apt-get install -y git zip bzip2 wget tar less \  
nodejs ruby ruby-dev \  
libtool \  
automake autoconf \  
fontconfig libicu-dev libfontconfig1 \  
libsqlite3-dev \  
openssh-client \  
$buildDeps --no-install-recommends \  
&& rm -r /var/lib/apt/lists/* \  
\  
&& docker-php-ext-install mcrypt zip pdo_mysql opcache \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached \  
&& rm -rf /tmp/pear \  
\  
&& npm -g install phantomjs-prebuilt \  
\  
&& apt-mark manual $doNotUninstall \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
  

