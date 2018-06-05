FROM php:7.1-alpine  
  
MAINTAINER Jonathan Daigle [https://github.com/daiglej]  
  
RUN docker-php-ext-install -j "$(getconf _NPROCESSORS_ONLN)" pcntl  
  
# Set locale to utf8 (TODO : does that work?)  
ENV LANG en_US.utf8  
ENV PGDATA /var/lib/postgresql/data  
#RUN apt-get update \  
# && apt-get install -y locales --no-install-recommends \  
# && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
# && locale-gen en_US.UTF-8 \  
# && /usr/sbin/update-locale LANG=en_US.UTF-8 \  
# && rm -rf /var/lib/apt/lists/*  
#ENV LC_ALL en_US.UTF-8  
# Install the latest version of git  
RUN apk add --no-cache --virtual .git-deps \  
g++ \  
make \  
autoconf \  
zlib-dev \  
openssl-dev \  
expat-dev \  
curl-dev \  
tcl-tls-dev \  
&& curl -O https://www.kernel.org/pub/software/scm/git/git-2.10.2.tar.gz \  
&& tar -xzf git-2.10.2.tar.gz \  
&& rm -f git-2.10.2.tar.gz \  
&& ( \  
cd git-2.10.2 \  
&& ./configure --prefix=/usr/local \  
&& make install \  
&& make clean \  
) \  
&& rm -fr git-2.10.2 \  
&& apk del .git-deps  
  
# Install auto pep8  
RUN apk add --no-cache py-pip \  
&& pip install --upgrade autopep8  
  
# Install js-beuatify https://github.com/beautify-web/js-beautify  
RUN apk add --no-cache py-pip \  
&& pip install --upgrade jsbeautifier  
  
# Install composer dependencies  
RUN apk add --no-cache gzip openssh-client patch  
  
RUN adduser -D real-beauty \  
&& mkdir /code /workdir \  
&& chown real-beauty /code /workdir  
  
USER real-beauty  
  
  
WORKDIR /code  
  
# Install composer packages  
COPY composer.* /code/  
RUN ./composer.phar install --no-dev --optimize-autoloader --classmap-
authoritative --no-interaction \  
&& rm -fr ~/.composer/ /code/composer.*  
  
COPY . /code  
RUN ./composer.phar dump-autoload \  
&& rm -fr ~/.composer/ /code/composer.*  
  
# fixme  
USER root  
RUN chmod +x /code/bin/*  
  
ENTRYPOINT ["php", "bin/docker-entry-point"]  
CMD []  

