FROM debian:jessie  
MAINTAINER Dries Hooghe <dries.hooghe@gmail.com>  
  
# Basic packages  
RUN apt-get update -y \  
&& apt-get install -y \  
wget \  
curl \  
zip \  
unzip \  
git \  
vim \  
rsync \  
iputils-ping \  
dnsutils \  
net-tools \  
xz-utils \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
openssl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Nginx  
RUN apt-get update -y \  
&& apt-get install -y \  
apache2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Node  
RUN wget https://nodejs.org/dist/v6.10.2/node-v6.10.2-linux-x64.tar.xz  
RUN tar xvfJ node-v6.10.2-linux-x64.tar.xz -C /opt  
RUN rm node-v6.10.2-linux-x64.tar.xz  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/node /usr/bin/node  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/node /usr/local/bin/node  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/npm /usr/bin/npm  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/npm /usr/local/bin/npm  
  
# Install Node dependencies  
RUN npm install -g grunt-cli@1.2.0 \  
yarn@1.3.2 \  
globals@11.0.1  
  
# Install PHP  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update -y \  
&& apt-get install -y \  
php7.1 \  
php7.1-curl \  
php7.1-fpm \  
php7.1-cli \  
php7.1-mysql \  
php7.1-mbstring \  
php7.1-dom \  
php7.1-json \  
php7.1-zip \  
php7.1-xdebug \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN sed -i -e "s:^.*cgi\\.fix_pathinfo=.*$:cgi.fix_pathinfo=0:g"
/etc/php/7.1/fpm/php.ini  
  
# Instal Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install PHPUnit  
RUN wget https://phar.phpunit.de/phpunit-6.4.phar  
RUN chmod +x phpunit-6.4.phar  
RUN mv phpunit-6.4.phar /usr/local/bin/phpunit  
  
# Install Open-SSH  
RUN apt-get update -y \  
&& apt-get install -y \  
openssh-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Expose ports  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3306  
# Copy files to container root and give scripts execution rights  
COPY files/root /  
RUN chmod +x /entrypoint.sh  
RUN chmod +x /start.sh  
  
# Prepare usage  
WORKDIR /opt  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/start.sh"]  

