FROM drupal:8.2.1-apache  
MAINTAINER laurent NGAKO <laurent.ngako@gmail.com>  
  
# Install vim and git  
RUN apt-get update -y \  
&& apt-get install vim -y \  
&& apt-get install git -y \  
&& apt-get install wget -y  
  
# Install composer  
WORKDIR /tmp  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
# Install drupalconsole  
RUN php -r "readfile('https://drupalconsole.com/installer');" > drupal.phar  
RUN mv drupal.phar /usr/local/bin/drupal  
RUN chmod +x /usr/local/bin/drupal  
  
# Add gosu  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates  
  
# Create src folder  
RUN mkdir -p /home/dev/app  
  
# Copy src  
COPY ./app /home/dev/app/  
  
# Create alias of the script to add dev USER  
RUN chmod +x /home/dev/app/conf/add-local-user.sh  
RUN ln -s /home/dev/app/conf/add-local-user.sh /usr/local/bin/add-local-user  
  
# Add custom php.ini  
RUN ln -s /home/dev/app/conf/php/php.ini /usr/local/etc/php/php.ini  
# Install last CA. Use Mozilla last certification pem file.  
RUN mkdir -p /usr/share/ca-certificates  
RUN cp /home/dev/app/conf/cert.pem /usr/share/ca-certificates/  
  
# Link src folders  
RUN rm -rf /var/www/html/modules  
RUN rm -rf /var/www/html/themes  
RUN rm -rf /var/www/html/profiles  
RUN rm -rf /var/www/html/sites  
RUN rm -f /var/www/html/composer.json  
  
RUN ln -s /home/dev/app/drupal-src/modules /var/www/html/modules  
RUN ln -s /home/dev/app/drupal-src/themes /var/www/html/themes  
RUN ln -s /home/dev/app/drupal-src/profiles /var/www/html/profiles  
RUN ln -s /home/dev/app/drupal-src/sites /var/www/html/sites  
RUN ln -s /home/dev/app/drupal-src/composer.json /var/www/html/composer.json  
  
# Set working directory  
WORKDIR /home/dev/app  
  

