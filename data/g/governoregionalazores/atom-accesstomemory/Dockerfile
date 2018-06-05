FROM ubuntu:16.04  
ENV ATOM_DIR=/usr/share/nginx/atom  
ENV ATOM_VERSION=2.3.1  
RUN apt-get update && apt-get install -y nginx  
  
RUN service nginx restart  
  
RUN apt-get install -y openjdk-8-jre-headless software-properties-common wget  
RUN wget -qO - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add -  
RUN add-apt-repository "deb
http://packages.elasticsearch.org/elasticsearch/1.7/debian stable main"  
RUN apt-get update && apt-get install -y elasticsearch  
RUN systemctl enable elasticsearch  
RUN service elasticsearch start  
  
ADD atom /etc/nginx/sites-available/atom  
RUN ln -sf /etc/nginx/sites-available/atom /etc/nginx/sites-enabled/atom  
RUN rm /etc/nginx/sites-enabled/default  
ADD atom.conf /  
  
RUN service elasticsearch restart  
  
RUN apt-get update && apt-get install -y php7.0-cli \  
php7.0-curl \  
php7.0-json \  
php7.0-ldap \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-readline \  
php7.0-xml \  
php7.0-fpm \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-xsl \  
php7.0-zip \  
php-memcache \  
php-apcu \  
php-dev \  
gearman-job-server \  
imagemagick \  
ghostscript \  
poppler-utils \  
ffmpeg \  
php-apcu \  
php-curl \  
php-pear  
  
RUN pecl install apcu_bc-beta  
RUN echo "extension=apc.so" | tee > /etc/php/7.0/mods-available/apcu-bc.ini  
  
RUN ln -sf /etc/php/7.0/mods-available/apcu-bc.ini
/etc/php/7.0/fpm/conf.d/30-apcu-bc.ini  
RUN ln -sf /etc/php/7.0/mods-available/apcu-bc.ini
/etc/php/7.0/cli/conf.d/30-apcu-bc.ini  
  
ADD atom.conf /etc/php/7.0/fpm/pool.d/atom.conf  
  
RUN wget https://storage.accesstomemory.org/releases/atom-$ATOM_VERSION.tar.gz  
RUN mkdir /usr/share/nginx/atom  
RUN tar xzf atom-$ATOM_VERSION.tar.gz -C /usr/share/nginx/atom --strip 1  
RUN chown -R www-data:www-data /usr/share/nginx/atom  
RUN apt-get install -y mysql-client php-mysql  
  
COPY bootstrap.php /bootstrap.php  
  
RUN service php7.0-fpm start  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod 777 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR $ATOM_DIR  
  
CMD ["nginx", "-g", "daemon off;"]  
  

