FROM php:7-alpine  
  
MAINTAINER Esther Weidauer <esther@selfawaresoup.com>  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-
init_1.0.2_amd64 /usr/bin/dumb-init  
RUN chmod +x /usr/bin/dumb-init  
  
RUN apk add --update \  
bash \  
git \  
openssl \  
wget \  
unzip \  
curl-dev \  
libxml2-dev \  
rsync \  
zlib-dev  
  
RUN docker-php-ext-install zip curl xml  
  
RUN wget -O /usr/bin/gitlab-ci-multi-runner https://gitlab-ci-multi-runner-
downloads.s3.amazonaws.com/latest/binaries/gitlab-ci-multi-runner-linux-amd64
&& \  
chmod +x /usr/bin/gitlab-ci-multi-runner && \  
ln -s /usr/bin/gitlab-ci-multi-runner /usr/bin/gitlab-runner && \  
mkdir /etc/gitlab-runner && \  
chmod -R 700 /etc/gitlab-runner  
  
ADD https://getcomposer.org/installer /tmp/composer-installer.php  
RUN php /tmp/composer-installer.php --install-dir=/usr/local/bin
--filename=composer && \  
rm /tmp/composer-installer.php  
  
RUN git clone https://github.com/sculpin/sculpin.git /usr/lib/sculpin && \  
cd /usr/lib/sculpin && \  
composer install && \  
ln -s /usr/lib/sculpin/bin/sculpin /usr/local/bin/sculpin  
  
ADD entrypoint.sh /entrypoint  
RUN chmod +x /entrypoint  
  
RUN mkdir /gitlab-runner  
  
VOLUME /data  
VOLUME /etc/gitlab-runner  
  
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]  
CMD ["run", "--working-directory=/gitlab-runner"]  

