# Use official php image.  
FROM php:7.1-cli  
ARG "version=3.0-dev"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
  
LABEL org.label-schema.vendor="Softonic" \  
org.label-schema.name="laravel-consumer" \  
org.label-schema.description="PHP CLI Docker image extension to use with
Laravel consumers" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/softonic/docker-laravel-
consumer/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd.devel="" \  
org.label-schema.build-date=$build_date  
  
# Installing required dependencies of laravel project.  
RUN apt-get update && apt-get install -y \  
libfcgi0ldbl \  
zlib1g-dev \  
libxml2-dev \  
libmcrypt-dev \  
git \  
&& docker-php-ext-install \  
zip \  
opcache \  
mbstring \  
pdo \  
pdo_mysql \  
mcrypt \  
mysqli \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer \  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
RUN composer global require "hirak/prestissimo:^0.3" --prefer-dist --no-
progress --no-suggest --optimize-autoloader --classmap-authoritative \  
&& composer clear-cache  
  
COPY rootfs/ /

