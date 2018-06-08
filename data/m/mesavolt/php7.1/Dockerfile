FROM debian:jessie  
  
# set debconf's default frontend mode to noninteractive  
# to prevent spamming the build logs with the same debconf error  
# debconf: unable to initialize frontend: Dialog  
# debconf: (No usable dialog-like program is installed, so the dialog based
frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line
76, <> line 4.)  
# debconf: falling back to frontend: Readline  
ENV DEBIAN_FRONTEND noninteractive  
  
# install base requirements  
RUN apt-get -qq update && apt-get -yqq install apt-utils apt-transport-https  
RUN apt-get -yqq install build-essential ca-certificates curl git
libfontconfig \  
libfreetype6-dev libjpeg62-turbo-dev libpng12-dev lsb-release \  
software-properties-common ssl-cert sudo unzip vim wget zip zlib1g-dev  
  
# add chrome/puppeteer dependencies  
# see
https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md#running-
puppeteer-in-docker  
RUN apt-get -yqq install gconf-service libasound2 libatk1.0-0 libc6 libcairo2
libcups2 \  
libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0
libglib2.0-0 \  
libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6
libx11-xcb1 \  
libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6
libxrandr2 \  
libxrender1 libxss1 libxtst6 fonts-liberation libappindicator1 libnss3 \  
xdg-utils  
  
# add php7 repo  
RUN curl -sS https://packages.sury.org/php/apt.gpg | apt-key add -  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
# add yarn repo  
RUN curl -sSL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list  
  
# add node repo  
RUN curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key
add -  
RUN echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list  
RUN echo "deb-src https://deb.nodesource.com/node_8.x jessie main" >>
/etc/apt/sources.list.d/nodesource.list  
  
# install php7.1  
RUN apt-get -qq update && apt-get -yqq install --no-install-recommends \  
php7.1 php7.1-fpm php7.1-bz2 php7.1-cli php7.1-common php7.1-curl php7.1-gd \  
php7.1-intl php7.1-json php7.1-mbstring php7.1-mysql php7.1-opcache
php7.1-readline \  
php7.1-sqlite3 php7.1-xml php7.1-zip php-gearman php-redis php-xdebug  
  
# set sensible php options  
RUN echo "date.timezone = Europe/Paris" >> /etc/php/7.1/cli/php.ini && \  
echo "memory_limit = 512M" >> /etc/php/7.1/cli/php.ini && \  
echo "error_reporting = E_ALL" >> /etc/php/7.1/cli/php.ini  
  
# install composer  
RUN curl -sSL https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# install phpunit  
RUN curl -sSL --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit.phar  
RUN chmod +x /usr/local/bin/phpunit  
  
# install node and yarn  
RUN apt-get -yqq install nodejs yarn  
  
# show installed packages info  
# redirect stderr to /dev/null because composer will complain about running it
as root  
RUN echo "node: " && node --version && \  
echo "yarn: " && yarn --version && \  
echo "php: " && php --version && \  
echo "php modules: " && php -m && \  
echo "phpunit: " && phpunit --version && \  
echo "composer: " && composer --version 2> /dev/null  
  
# add mesavolt user  
RUN adduser --disabled-password --gecos "" mesavolt  
  
# enable user mesavolt to run sudo with no password  
RUN echo "mesavolt ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/mesavolt && \  
chmod 0440 /etc/sudoers.d/mesavolt && visudo -c  
RUN service sudo restart  
  
# reset DEBIAN_FRONTEND var  
ENV DEBIAN_FRONTEND teletype  
  
# switch to mesavolt user (some tools complain when ran as root)  
USER mesavolt  
WORKDIR /home/mesavolt  

