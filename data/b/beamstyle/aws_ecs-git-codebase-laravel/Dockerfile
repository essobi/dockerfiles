FROM beamstyle/aws_ecs-git  
MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>  
  
# Install some basic dependencies  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
git \  
zip \  
unzip \  
wget  
  
# Install packages.  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
RUN wget https://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
RUN apt-get update && apt-get install -y \  
libapache2-mod-php7.0 \  
php7.0-fpm \  
php7.0-common \  
php7.0-cli \  
php7.0-sqlite3 \  
php-pear \  
php7.0-curl \  
php7.0-gd \  
php7.0-gmp \  
php7.0-intl \  
php7.0-imap \  
php7.0-json \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-mysqlnd \  
php7.0-ps \  
php7.0-readline \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xml \  
php7.0-zip \  
php7.0-xsl \  
cron \  
gettext \  
&& apt-get --purge autoremove  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
ADD auth.json /tmp/auth.json  
  
ENTRYPOINT ["sh", "-c"]  
  
# Running the custom script file "run.sh"  
ADD run.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
  
CMD ["/usr/local/bin/run.sh"]  

