FROM php:7.0-apache  
RUN apt-get update \  
&& apt-get install -yq git postgresql-client libpq-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo pdo_pgsql \  
&& a2enmod rewrite \  
&& docker-php-source delete  
RUN git clone https://github.com/iimog/wikidata-game-flower-color /wikidata-
game-flower-color  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
COPY php.ini /usr/local/etc/php/  
COPY parameters.yml /wikidata-game-flower-color/app/config/  
RUN cd /wikidata-game-flower-color; composer install  
RUN rm -rf /var/www/html && ln -fs /wikidata-game-flower-color/web
/var/www/html  
RUN chown -R www-data:www-data /wikidata-game-flower-color/var  

