FROM php:7.1-fpm  
MAINTAINER Kevin ARBOUIN <dev@arbouin-consulting.com>  
  
RUN apt-get update \  
&& apt-get install -yqq \  
vim \  
libicu-dev \  
libcurl4-openssl-dev \  
zlib1g-dev \  
git git-core \  
gcc make autoconf libc-dev pkg-config \  
zlib1g-dev \  
curl \  
zsh \  
wget \  
python \  
python-pip \  
unzip \  
libpng12-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libxrender1 \  
libfontconfig \  
libxtst6 \  
xz-utils  
  
RUN curl
"https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz" \  
&& tar Jxvf wkhtmltopdf.tar.xz \  
&& mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf  
  
RUN docker-php-ext-install \  
opcache \  
intl \  
mbstring \  
pdo_mysql \  
zip \  
json \  
curl \  
sockets \  
bcmath \  
gd \  
&& pecl install xdebug \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& php -r "readfile('https://getcomposer.org/installer');" | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer \  
&& apt-get clean  
  
RUN bash -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" \  
&& sed -i -- 's/robbyrussell/wezm+/g' /root/.zshrc \  
&& echo "source /root/.oh-my-zsh/oh-my-zsh.sh" >> ~/.zshrc \  
&& sed -i -- 's/git/git git-flow git-extras symfony2 command-not-found
composer/g' ~/.zshrc \  
&& echo 'export
PATH=$HOME/bin:/usr/local/bin:/usr/local/sbin:$HOME/.composer/vendor/bin:$PATH'
>> ~/.bashrc \  
&& echo 'export
PATH=$HOME/bin:/usr/local/bin:/usr/local/sbin:$HOME/.composer/vendor/bin:$PATH'
>> ~/.zshrc \  
&& echo "alias sf='bin/console'" >> ~/.bashrc \  
&& echo "alias ls='ls --color'" >> ~/.bashrc \  
&& echo "alias ll='ls -l'" >> ~/.bashrc \  
&& echo "alias la='ls -la'" >> ~/.bashrc  
  
ENV TERM=xterm  
  

