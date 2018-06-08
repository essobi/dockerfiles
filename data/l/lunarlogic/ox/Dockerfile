FROM ubuntu:14.04  
MAINTAINER Lunar Logic <support@lunarlogic.com>  
  
#Mongo PHP driver version  
ENV MONGO_VERSION 3.0.14  
ENV MONGO_PGP 3.0  
ENV MONGO_PHP_VERSION 1.6.14  
#Install php and dependenceis  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install \  
curl \  
git \  
make \  
apache2 \  
libapache2-mod-php5 \  
php5 \  
php5-dev \  
php5-gd \  
php5-curl \  
php5-mcrypt \  
php-pear \  
php-apc && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz" -o mongo.tgz \  
&& curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz.sig" -o mongo.tgz.sig \  
&& curl -SL "https://www.mongodb.org/static/pgp/server-$MONGO_PGP.asc" -o
server-$MONGO_PGP.asc \  
&& gpg --import server-$MONGO_PGP.asc \  
&& gpg --verify mongo.tgz.sig \  
&& tar -xvf mongo.tgz -C /usr/local \--strip-components=1 \  
&& rm mongo.tgz*  
  
RUN pecl install mongo-$MONGO_PHP_VERSION && \  
mkdir -p /etc/php5/mods-available && \  
echo "extension=mongo.so" > /etc/php5/mods-available/mongo.ini && \  
ln -s /etc/php5/mods-available/mongo.ini /etc/php5/cli/conf.d/mongo.ini && \  
ln -s /etc/php5/mods-available/mongo.ini /etc/php5/apache2/conf.d/mongo.ini &&
\  
ln -s /etc/php5/mods-available/mcrypt.ini /etc/php5/cli/conf.d/mcrypt.ini && \  
ln -s /etc/php5/mods-available/mcrypt.ini /etc/php5/apache2/conf.d/mcrypt.ini  
  
RUN a2enmod rewrite  
RUN rm -f /etc/apache2/sites-enabled/000-default.conf  
  
ADD run.sh /run.sh  
  
VOLUME ["/var/log/apache2"]  
  
EXPOSE 80  
CMD ["/run.sh"]  

