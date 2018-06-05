# TODO: use https://gist.github.com/Xotabu4/a243d9ff25cfe276bcaa0175fb6a4b00  
FROM alpine:edge  
  
RUN apk add \--no-cache \  
nodejs nodejs-npm unzip curl php7 php7-xml php7-mbstring php7-intl php7-curl
php7-tokenizer php7-dom php7-pdo php7-pdo_sqlite \  
php7-openssl php7-json php7-phar php7-zlib php7-ctype php7-pcntl php7-posix
php7-session php7-iconv php7-simplexml \  
python \  
build-base \  
git \  
bash \  
openjdk8-jre-base \  
# chromium dependencies  
udev \  
ttf-freefont \  
chromium-chromedriver \  
chromium && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chmod +x /usr/local/bin/composer && \  
rm -rf /var/cache/apk/* && \  
npm i -g npm

