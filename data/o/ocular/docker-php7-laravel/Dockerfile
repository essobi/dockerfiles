FROM alpine:3.6  
RUN apk --update add wget curl git php7-common php7-zlib php7-tokenizer
php7-xmlwriter php7-mbstring php7-curl php7-openssl php7-json php7-phar
php7-dom php7-session php7-zip php7-bz2 bash php7-mysqli php7-pdo_mysql
php7-sqlite3 php7-mcrypt php7-ctype php7-xml php7-pcntl php7-posix
php7-fileinfo php7-gd python fontconfig --repository
http://nl.alpinelinux.org/alpine/v3.6/community/ && rm /var/cache/apk/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN mkdir -p /var/www  
  
WORKDIR /var/www  
  
COPY . /var/www  
  
VOLUME /var/www  
  
CMD ["/bin/sh"]  
  
ENTRYPOINT ["/bin/sh", "-c"]

