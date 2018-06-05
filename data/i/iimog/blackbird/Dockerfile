FROM ubuntu:16.04  
# Install required packages  
RUN apt-get update && apt-get --assume-yes install \  
apache2 \  
git \  
php \  
curl \  
php-dev \  
php-curl \  
libapache2-mod-php \  
zip \  
nodejs \  
npm \  
imagemagick \  
sqlite3 \  
php7.0-sqlite3  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install bower  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g bower  
RUN npm install -g coffee-script  
  
# Prepare apache  
RUN rm -rf /var/www/html  
  
# Make terminal functional by default  
RUN echo "export TERM=xterm" >>/root/.bashrc  
  
# Install biom via conda  
RUN curl -sS http://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh >miniconda.sh  
RUN chmod +x miniconda.sh  
RUN ./miniconda.sh -b -f -p /usr/local  
RUN echo "export LC_ALL=C.UTF-8" >>/etc/apache2/envvars  
RUN echo "export LANG=C.UTF-8" >>/etc/apache2/envvars  
  
# Clone git repo  
RUN git clone https://github.com/molbiodiv/Blackbird.git /var/www/html  
RUN cd /var/www/html && composer install  
RUN cd /var/www/html && bower install --allow-root  
RUN cd /var/www/html && coffee -o scripts -c src  
RUN cd /var/www/html/vendor/iimog/biom-conversion-server && conda install
--yes --file explicit-conda-spec.txt  
RUN cp /var/www/html/vendor/iimog/biom-conversion-server/convert.php
/var/www/html  
RUN cd /var/www/html/biomFiles/ && sqlite3 blackbird.sqlite
<../data/dbschema.sql  
RUN chown -R www-data:www-data /var/www/html/biomFiles  
RUN cp /var/www/html/server/dbconfig-sqlite.php
/var/www/html/server/dbconfig.php  
  
# Add custom php ini  
ADD php.ini /etc/php/7.0/apache2/php.ini  
# Add custom apache conf  
ADD apache2.conf /etc/apache2/apache2.conf  
  
CMD service apache2 start; while true; do sleep 60; done  

