FROM alpine:edge  
  
RUN set -xe \  
echo 'http://dl-4.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache --update \  
bash \  
less \  
vim \  
sudo \  
nano \  
php7 \  
php7-fpm \  
php7-cli \  
php7-json \  
php7-zlib \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-pdo \  
php7-phar \  
php7-openssl \  
php7-pdo_mysql \  
php7-mysqli \  
php7-session \  
php7-gd \  
php7-iconv \  
php7-mcrypt \  
php7-curl \  
php7-opcache \  
php7-ctype \  
php7-apcu \  
php7-intl \  
php7-bcmath \  
php7-mbstring \  
php7-dom \  
php7-xmlreader \  
php7-gettext \  
php7-tokenizer \  
php7-zip \  
openssh-client \  
git \  
curl \  
wget \  
rsync \  
musl \  
tar \  
autoconf \  
automake \  
binutils \  
binutils-libs \  
build-base \  
file \  
fortify-headers \  
g++ \  
gcc \  
gdbm \  
gmp \  
sqlite-libs \  
yaml \  
zlib-dev \  
gmp-dev \  
http-parser \  
isl \  
libatomic \  
libc-dev \  
libffi \  
libgmpxx \  
libgomp \  
libintl \  
libjpeg-turbo-utils \  
libmagic \  
libuv \  
m4 \  
make \  
mpc1 \  
mpfr3 \  
musl-dev \  
nasm \  
nodejs \  
openssh-keygen \  
perl \  
pkgconf \  
python2 \  
sqlite-libs \  
sqlite-dev \  
yaml \  
mysql-client \  
zlib-dev && \  
sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php7/php.ini && \  
ln -sf /usr/bin/php7 /usr/bin/php  
  
## ADD PHP to the path  
ENV PATH=$PATH:/usr/bin/php  
  
COPY www.conf /etc/php7/php-fpm.conf  
  
CMD "echo 'Codeception server started'"

