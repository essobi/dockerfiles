FROM docker  
MAINTAINER William Hearn <sylus1984@gmail.com>  
  
# Custom additions for test runner.  
RUN apk --update add \  
bash \  
ca-certificates \  
curl \  
git \  
make \  
openssh-client \  
patch \  
tar  
  
# Docker Compose with glibc bypass.  
RUN curl -Lo /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
curl -Lo glibc.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \  
curl -Lo glibc-bin.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-bin-2.23-r3.apk && \  
apk add glibc.apk glibc-bin.apk  
  
# Install PHP.  
RUN apk --no-cache --update --repository=http://dl-
cdn.alpinelinux.org/alpine/edge/main add \  
libressl && \  
apk --no-cache --update --repository=http://dl-
cdn.alpinelinux.org/alpine/edge/community add \  
php7 \  
php7-xml \  
php7-xsl \  
php7-pdo_mysql \  
php7-mcrypt \  
php7-curl \  
php7-json \  
php7-fpm \  
php7-phar \  
php7-openssl \  
php7-mysqli \  
php7-ctype \  
php7-opcache \  
php7-mbstring \  
php7-zip \  
php7-zlib  
  
# Correct paths.  
RUN ln -s /etc/php7 /etc/php && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
ln -s /usr/lib/php7 /usr/lib/php  
  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Docker Compose.  
RUN curl -Lo docker-compose
https://github.com/docker/compose/releases/download/1.8.1/docker-compose-
Linux-x86_64 && \  
chmod +x docker-compose && \  
mv docker-compose /usr/local/bin  
  
# Install Go Jira.  
RUN curl -Lo jira https://github.com/Netflix-Skunkworks/go-
jira/releases/download/v0.1.9/jira-linux-amd64 && \  
chmod +x jira && \  
mv jira /usr/local/bin  
  
# Security fix for CVE-2016-0777 and CVE-2016-0778  
RUN echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

