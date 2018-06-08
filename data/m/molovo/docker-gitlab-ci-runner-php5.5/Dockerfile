# docker-gitlab-ci-runner-php5.5  
FROM molovo/docker-gitlab-ci-runner-php  
MAINTAINER James Dinsdale "hi@molovo.co"  
ENV PHP_VERSION 5.5.22  
COPY files/ci-runner.ini /root/.phpenv/versions/$PHP_VERSION/etc/conf.d/ci-
runner.ini  
  
RUN phpenv install $PHP_VERSION \  
phpenv rehash && \  
phpenv global $PHP_VERSION  
  
# Install PHP PECL extensions  
RUN yes '' | pecl install \  
intl \  
mcrypt \  
mongo \  
redis \  
memcache \  
ssh2-0.12 \  
xdebug \  
xhprof  
  
RUN echo "extension='redis.so'" >> ~/.phpenv/versions/$(phpenv version-
name)/etc/conf.d/ci-runner.ini  
RUN composer self-update  
RUN composer global require --prefer-source "codeception/codeception"  
RUN composer global require --prefer-source "codeception/verify"  
RUN composer global require --prefer-source "codeception/specify"  

