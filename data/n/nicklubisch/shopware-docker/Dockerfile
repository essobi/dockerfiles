FROM ubuntu:xenial  
MAINTAINER Nick Lubisch <nicklubisch@online.de>  
  
#ENV SHOPWARE  
ENV SW_GIT_TAG latest  
  
#ENV SSH  
ENV SSH_USER shopware  
ENV SSH_PASS shopware  
  
#ENV_APACHE  
ENV APACHE_ROOT_DIR /var/www/shopware  
  
#ENV MYSQL  
ENV MYSQL_HOST localhost  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER shopware  
ENV MYSQL_PASS shopware  
ENV MYSQL_DBNAME shopware  
  
#ENV PHP  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Install packages  
RUN echo "Install Packages"  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q -y update > /dev/null  
RUN apt-get -q -y upgrade > /dev/null  
RUN apt-get -q install -y software-properties-common > /dev/null  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php > /dev/null  
RUN apt-get update > /dev/null  
RUN apt-get -y -q install \  
supervisor \  
sudo \  
bash-completion \  
git \  
htop \  
tree \  
vim \  
nano \  
curl \  
zip \  
rsync \  
wget \  
ant \  
mysql-server \  
mysql-client \  
openssh-server \  
libapache2-mod-php5.6 \  
php5.6-cli \  
php5.6-curl \  
php5.6-gd \  
php5.6-mysql \  
php5.6-mbstring \  
php5.6-simplexml \  
php5.6-xml \  
php5.6-zip \  
php5.6-soap \  
libapache2-mod-php7.0 \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-simplexml \  
php7.0-xml \  
php7.0-zip \  
php7.0-soap \  
libapache2-mod-php7.1 \  
php7.1-cli \  
php7.1-curl \  
php7.1-gd \  
php7.1-mysql \  
php7.1-mbstring \  
php7.1-simplexml \  
php7.1-xml \  
php7.1-zip \  
php7.1-soap \  
php-apcu \  
php-xdebug \  
nodejs \  
npm \  
> /dev/null  
  
#Create symlink for node  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
#Install npm packages  
RUN npm install -g grunt-cli  
  
#Install SW CLI Tools  
RUN wget http://shopwarelabs.github.io/sw-cli-tools/sw.phar  
RUN mv sw.phar /usr/bin/sw  
RUN chmod 755 /usr/bin/sw  
  
#Configure Apache  
RUN echo "Configure Apache"  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
ADD docker/apache/apache_default /etc/apache2/sites-available/000-default.conf  
RUN sed -i -e "s|APACHE_ROOT_DIR|${APACHE_ROOT_DIR}|" /etc/apache2/sites-
available/000-default.conf  
RUN a2enmod rewrite autoindex  
RUN mkdir -p ${APACHE_ROOT_DIR}  
RUN touch ${APACHE_ROOT_DIR}/index.html  
RUN echo "Hello World" >> ${APACHE_ROOT_DIR}/index.html  
RUN /etc/init.d/apache2 start  
  
#Configure PHP5.6/7.0/7.1  
RUN echo "Configure PHP"  
RUN sed -ri -e "s/^upload_max_filesize.*/upload_max_filesize =
${PHP_UPLOAD_MAX_FILESIZE}/" -e "s/^post_max_size.*/post_max_size =
${PHP_POST_MAX_SIZE}/" /etc/php/5.6/apache2/php.ini  
RUN sed -ri -e "s/^upload_max_filesize.*/upload_max_filesize =
${PHP_UPLOAD_MAX_FILESIZE}/" -e "s/^post_max_size.*/post_max_size =
${PHP_POST_MAX_SIZE}/" /etc/php/7.0/apache2/php.ini  
RUN sed -ri -e "s/^upload_max_filesize.*/upload_max_filesize =
${PHP_UPLOAD_MAX_FILESIZE}/" -e "s/^post_max_size.*/post_max_size =
${PHP_POST_MAX_SIZE}/" /etc/php/7.1/apache2/php.ini  
  
#Configure MySQL  
RUN echo "Configure MySQL"  
ADD docker/mysql/my.cnf /etc/mysql/my.cnf  
#  
##Configure SSH  
RUN echo "Configure SSH"  
RUN mkdir /var/run/sshd  
RUN chmod 0755 /var/run/sshd  
RUN useradd -d /var/www/ --shell /bin/bash --groups sudo "$SSH_USER"  
RUN echo "$SSH_PASS\n$SSH_PASS" | passwd "$SSH_USER"  
RUN sed -ri -e "s/PermitRootLogin/#PermitRootLogin/" /etc/ssh/sshd_config  
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config  
  
#Add composer  
RUN echo "Add composer"  
RUN wget https://getcomposer.org/installer -P /tmp  
RUN cat /tmp/installer | php -- --install-dir=/usr/bin  
RUN mv /usr/bin/composer.phar /usr/bin/composer  
RUN chmod a+x /usr/bin/composer  
  
#Add bash scripts and make them executable  
RUN echo "Add bash scripts"  
COPY docker/bash/install_shopware.sh /install_shopware.sh  
COPY docker/bash/mysql.sh /mysql.sh  
COPY docker/bash/startup.sh /startup.sh  
COPY docker/bash/entrypoint.sh /entrypoint.sh  
RUN chmod 755 /*.sh  
  
RUN echo "root\nroot" | passwd  
ADD /docker/supervisor/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
ENV SW_GIT_TAG v5.2.0  
ENTRYPOINT /entrypoint.sh  
EXPOSE 22 80 3306  

