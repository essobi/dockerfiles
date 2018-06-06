# CAVALERIE WEB SERVER  
#  
# Web server dedicated to La Cavalerie websites  
# Inspiration: tutum/apache-php image  
FROM lacavalerie/base-web-stack  
MAINTAINER Arnaud Lenglet <arnaud@agencecavalerie.com>  
  
# ------------ BASE PACKAGES INSTALLATION ------------  
RUN apt-get update && apt-get install -y \  
apache2 \  
php5  
  
RUN rm -rf /var/lib/apt/lists/* && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# ------------ WP CLI INSTALLATION ------------  
RUN mkdir /wp-cli  
WORKDIR /wp-cli  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
  
# ------------ COPY SCRIPTS + CHMOD ------------  
COPY scripts/* /scripts/  
RUN chmod 755 /scripts/*  
  
# ------------ CREATE APPS FOLDER + EXPOSE PORT 80 + LAUNCH SCRIPT
------------  
WORKDIR /scripts  
EXPOSE 80  
CMD ["/scripts/setup.rb"]

