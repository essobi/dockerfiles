FROM phusion/baseimage:latest  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
#add repo with newest PHP versions  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
  
#add nodejs  
RUN curl -sL https://deb.nodesource.com/setup_9.x -o nodesource_setup.sh  
RUN bash nodesource_setup.sh  
RUN apt-get install -y nodejs  
RUN apt-get install -y build-essential  
  
#add yarn repo  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv D101F7899D41F3C3  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
#  
RUN apt-get update  
  
# Install PHP 7.2, some PHP extentions and some useful Tools with APT  
RUN apt-get install -y \  
acl \  
mysql-client \  
nginx \  
php7.2-bcmath \  
php7.2-cli \  
php7.2-common \  
php7.2-curl \  
php7.2-fpm \  
php7.2-gd \  
php7.2-intl \  
php7.2-json \  
php7.2-mbstring \  
php7.2-mysql \  
php7.2-xml \  
php7.2-zip \  
php7.2-soap \  
php7.2-apcu \  
php7.2-sqlite3 \  
php-imagick \  
php-memcached \  
php-mongodb \  
php-redis \  
php-zip  
  
# Install additional tools  
RUN apt-get install -y \  
openjdk-8-jdk \  
ant \  
git \  
curl \  
python-pip \  
zip \  
joe \  
jq  
  
RUN apt-get install -y \  
wget unzip libmcrypt-dev libpng-dev libjpeg-dev \  
ghostscript zbar-tools dmtx-utils poppler-utils \  
tesseract-ocr qpdf pdftk netcat  
  
RUN wget -q https://github.com/coherentgraphics/cpdf-
binaries/raw/17372d86935f7541ae0bc7ff0b9eebb721af0cb0/Linux-Intel-64bit/cpdf
-O /usr/local/bin/cpdf && chmod +x /usr/local/bin/cpdf  
  
RUN pip install awscli  
  
# Install docker client  
ENV DOCKER_VERSION="18.03.0-ce"  
RUN curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz
\  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/bin  
  
# Add dockerize  
ENV DOCKERIZE_VERSION v0.6.1  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
#Set up PHP7-FPM folder  
RUN mkdir /run/php  
RUN chmod 777 /run/php/  
  
#Install lastest version of npm  
RUN npm install npm -g  
  
#Install yarn  
RUN apt-get install -y yarn  
  
# Add a symbolic link for Node  
#RUN ln -s /usr/bin/nodejs /usr/bin/node  
# Add convenience aliaseses  
RUN echo "alias phpunit='./bin/phpunit'" >> ~/.bashrc  
RUN echo "alias phpspec='./bin/phpspec'" >> ~/.bashrc  
RUN echo "alias behat='./bin/behat'" >> ~/.bashrc  
RUN echo 'alias sf="bin/console"' >> ~/.bashrc  
RUN echo 'alias cc="bin/console cache:clear"' >> ~/.bashrc  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Source the bash  
RUN . ~/.bashrc  
  
#Delete enabled Nginx sites  
RUN rm -rf /etc/nginx/sites-enabled/*  
  
#Delete everything from /var/www/ folder  
RUN rm -rf /var/www/*  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /install  
  
WORKDIR /var/www  

