FROM debian:stretch-slim  
#docker build --rm --memory=1g --memory-swap=1g -t wp-tests:latest .  
MAINTAINER Hendrawan Kuncoro "pentatonicfunk@gmail.com"  
ENV HOME="/root"  
RUN apt update -y && \  
apt install \  
build-essential \  
ssh \  
curl \  
git \  
subversion \  
wget \  
gnupg \  
php-cli \  
php-dev \  
php-pear \  
autoconf \  
automake \  
libcurl3-openssl-dev \  
libxslt1-dev \  
mcrypt \  
libmcrypt-dev \  
libmhash-dev \  
re2c \  
libxml2 \  
libxml2-dev \  
bison \  
libbz2-dev \  
libreadline-dev \  
libicu-dev \  
libpng-dev \  
gettext \  
libmcrypt-dev \  
libmcrypt4 \  
libmhash-dev \  
libmhash2 \  
libmariadbclient-dev-compat \  
libmariadbclient-dev \  
mysql-client \  
mysql-server -y \  
\--no-install-recommends && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash && \  
apt install -y nodejs && \  
apt install -y sass --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -L -O https://github.com/phpbrew/phpbrew/raw/1.23.1/phpbrew && \  
chmod +x phpbrew && \  
mv phpbrew /usr/local/bin  
  
#add repos to known hosts  
RUN mkdir -p ~/.ssh  
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts  
RUN ssh-keyscan -t rsa bitbucket.org >> ~/.ssh/known_hosts  
  
#curl symlink  
RUN ln -s /usr/include/x86_64-linux-gnu/curl /usr/include/curl  
  
#phpbrew install  
RUN phpbrew init \  
&& /bin/bash -c "source ~/.phpbrew/bashrc"; exit 0  
  
#get older php  
RUN phpbrew known --old;  
  
RUN phpbrew install 7.2.3 \  
+bcmath +bz2 +calendar \  
+cli +ctype +curl +dom +fileinfo \  
+filter +gd +gettext \  
+icu +imap +ipc \  
+json +mbregex +mbstring \  
+mcrypt +mhash +mysql \  
+opcache +pcntl +pcre \  
+pdo +pear +phar +posix +readline +soap \  
+sockets +tokenizer +xml +zip +openssl  
  
RUN rm -rf $HOME/.phpbrew/build/*  
  
RUN cd $HOME && \  
#phpunit-6  
wget -O phpunit-6 https://phar.phpunit.de/phpunit-6.5.7.phar && \  
chmod +x phpunit-6  
#reset mysql password  
COPY scripts/reset_mysql.sql /root/reset_mysql.sql  
RUN service mysql start && \  
mysql -u root < $HOME/reset_mysql.sql  
  
#phpunit-multi script  
COPY scripts/phpunit.sh /root/phpunit.sh  
RUN chmod +x $HOME/phpunit.sh && \  
mv $HOME/phpunit.sh /usr/local/bin/phpunit  
  
COPY entrypoint.sh /root/entrypoint.sh  
ENTRYPOINT ["/root/entrypoint.sh"]  

